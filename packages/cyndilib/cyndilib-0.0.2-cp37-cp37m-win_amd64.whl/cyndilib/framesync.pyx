cimport cython
from libc.math cimport lround

import threading

from .clock cimport time, sleep


__all__ = (
    'FrameSync', 'FrameSyncThread',
    'FrameSyncWorker', 'VideoWorker', 'AudioWorker',
)


cdef class FrameSync:
    """A wrapper around the |NDI| frame synchronization module

    When receiving streams, the frame sync methods in the |NDI| library use
    various buffering and clock-timing techniques to keep video and audio
    data in sync with each other.

    Timing "jitter" between capture calls is also accounted for which reduces
    the amount of critically-timed application code as compared to the direct
    approach needed for :class:`~.receiver.Receiver`.

    .. note::

        Instances of this class are automatically created by the
        :class:`~receiver.Receiver` and therefore not intended to be created
        directly.

    Attributes:
        video_frame (VideoFrameSync):
        audio_frame (AudioFrameSync):


    """
    def __cinit__(self, Receiver receiver, **kwargs):
        self.receiver = receiver
        cdef NDIlib_recv_instance_t recv_ptr = receiver.ptr
        if recv_ptr is NULL:
            raise ValueError('Receiver has no pointer')
        self.ptr = NDIlib_framesync_create(recv_ptr)
        if self.ptr is NULL:
            raise MemoryError()

    def __dealloc__(self):
        cdef NDIlib_framesync_instance_t ptr = self.ptr
        if ptr is not NULL:
            self.ptr = NULL
            NDIlib_framesync_destroy(ptr)

    def set_video_frame(self, VideoFrameSync video_frame):
        """Set the :attr:`video_frame`
        """
        self._set_video_frame(video_frame)

    def set_audio_frame(self, AudioFrameSync audio_frame):
        """Set the :attr:`audio_frame`
        """
        self._set_audio_frame(audio_frame)

    def capture_video(self, FrameFormat fmt = FrameFormat.progressive):
        """Capture video

        After this call, the captured data will be available in the
        :attr:`video_frame`
        """
        self._capture_video(fmt)

    def capture_available_audio(self) -> int:
        """Capture all available audio samples

        After this call, the captured data will be available in the
        :attr:`audio_frame`

        Returns the number of samples captured
        """
        return self._capture_available_audio()

    def capture_audio(self, size_t no_samples) -> int:
        """Capture available audio samples up to *no_samples*

        After this call, the captured data will be available in the
        :attr:`audio_frame`

        Returns the number of samples captured
        """
        return self._capture_audio(no_samples)

    def audio_samples_available(self) -> int:
        """Get the number of audio samples currently available for capture
        """
        return self._audio_samples_available()

    cdef void _set_video_frame(self, VideoFrameSync video_frame) except *:
        self.video_frame = video_frame

    cdef void _set_audio_frame(self, AudioFrameSync audio_frame) except *:
        self.audio_frame = audio_frame

    cdef int _audio_samples_available(self) nogil except *:
        return NDIlib_framesync_audio_queue_depth(self.ptr)

    cdef void _capture_video(self, FrameFormat fmt = FrameFormat.progressive) except *:
        cdef NDIlib_video_frame_v2_t* video_ptr = self.video_frame.ptr
        self._do_capture_video(video_ptr, fmt)
        self.video_frame._process_incoming(self.ptr)

    cdef size_t _capture_available_audio(self) except *:
        cdef size_t no_samples = self._audio_samples_available()
        if no_samples == 0:
            return 0
        return self._capture_audio(no_samples, False)

    cdef size_t _capture_audio(self, size_t no_samples, bint limit=True, bint truncate=True) except *:
        cdef NDIlib_audio_frame_v3_t* audio_ptr = self.audio_frame.ptr
        cdef size_t num_available
        if limit:
            num_available = self._audio_samples_available()
            if num_available == 0:
                return 0
            elif num_available < no_samples:
                if not truncate:
                    return 0
                no_samples = num_available
        self._do_capture_audio(audio_ptr, no_samples)
        self.audio_frame._process_incoming(self.ptr)
        return no_samples

    cdef void _do_capture_video(
        self,
        NDIlib_video_frame_v2_t* video_ptr,
        FrameFormat fmt = FrameFormat.progressive,
    ) nogil except *:
        cdef NDIlib_frame_format_type_e _fmt = frame_format_cast(fmt)
        NDIlib_framesync_capture_video(self.ptr, video_ptr, _fmt)

    cdef void _do_capture_audio(
        self,
        NDIlib_audio_frame_v3_t* audio_ptr,
        size_t no_samples,
    ) nogil except *:
        NDIlib_framesync_capture_audio_v2(
            self.ptr, audio_ptr,
            audio_ptr.sample_rate, audio_ptr.no_channels, no_samples,
        )

    cdef void _free_video(self, NDIlib_video_frame_v2_t* video_ptr) nogil except *:
        NDIlib_framesync_free_video(self.ptr, video_ptr)

    cdef void _free_audio(self, NDIlib_audio_frame_v3_t* audio_ptr) nogil except *:
        NDIlib_framesync_free_audio_v2(self.ptr, audio_ptr)


cdef class FrameSyncWorker():
    """Worker for :class:`FrameSyncThread`

    Attributes:
        frame_sync (FrameSync): The parent FrameSync instance
        running (bool): Current run state
        callback (Callback): Callback triggered when a new frame is available
        target_fps (float): The target frame rate
        target_interval (float): Interval between frames defined as :math:`1/F_r`
        frame_rate (fractions.Fraction): The current frame rate

    """
    cdef FrameSync frame_sync
    cdef Event wait_event
    cdef bint running
    cdef Callback callback
    cdef double target_fps
    cdef double target_interval
    cdef double next_timestamp
    cdef frame_rate_t frame_rate

    def __cinit__(self, *args, **kwargs):
        self.target_fps = 9
        self.target_interval = 1 / 9.0
        self.next_timestamp = -1
        self.frame_rate.numerator = 1
        self.frame_rate.denominator = 100

    def __init__(self, FrameSync frame_sync):
        self.frame_sync = frame_sync
        self.callback = Callback()
        self.wait_event = Event()

    cdef run(self):
        self.running = True
        cdef double now
        cdef bint captured = False
        cdef double wait_time
        while self.running:
            try:
                if not self.has_frame() or not self.frame_sync.receiver._is_connected():
                    self.next_timestamp = -1
                    self.wait_for_evt(.1)
                    continue
                now = self.now()


                if (self.can_capture() and
                    self.next_timestamp >= now or self.next_timestamp == -1):

                    captured = self.do_capture()
                    if captured:
                        self.trigger_callback()
                    self.next_timestamp = self.calc_next_ts(self.now())

                else:
                    wait_time = self.next_timestamp - now
                    if wait_time <= 0:
                        print(f'wait time: {wait_time}')
                        self.next_timestamp = self.calc_next_ts(self.now())
                        continue
                    self.wait_for_evt(wait_time)
            except:
                import traceback
                traceback.print_exc()
                break

    cdef void trigger_callback(self) except *:
        """Trigger the :attr:`callback` if set
        """
        if self.callback.has_callback:
            self.callback.trigger_callback()

    cdef void time_sleep(self, double timeout) except *:
        sleep(timeout)

    cdef double now(self) except *:
        return time()

    cdef void wait_for_evt(self, double timeout) except *:
        self.wait_event.wait(timeout)
        self.wait_event.clear()

    cdef bint has_frame(self) except *:
        return False

    cdef bint can_capture(self) except *:
        return False

    cdef bint do_capture(self) except *:
        pass

    cdef void update_fps(self) except *:
        pass

    cdef double calc_next_ts(self, double now) except *:
        if self.target_fps == 9:
            self.update_fps()
        return now + self.target_interval

    cdef void stop(self) except *:
        self.wait_event.set()
        self.running = False


cdef class VideoWorker(FrameSyncWorker):
    """Worker used by :class:`FrameSyncThread` for video frames
    """
    cdef VideoFrameSync video_frame

    cdef bint can_capture(self) except *:
        return True

    cdef bint do_capture(self) except *:
        self.frame_sync._capture_video()
        return True

    cdef bint has_frame(self) except *:
        if self.video_frame is not None:
            return True
        if self.frame_sync.video_frame is not None:
            self.video_frame = self.frame_sync.video_frame
            return True
        return False

    @cython.cdivision(True)
    cdef void update_fps(self) except *:
        cdef frame_rate_t* fr = self.video_frame._get_frame_rate()
        self.frame_rate.numerator = fr.numerator
        self.frame_rate.denominator = fr.denominator
        if fr.denominator <= 0 or fr.numerator == 0:
            self.target_fps = 9
            self.target_interval = 1 / 30.
        else:
            self.target_fps = fr.numerator / <double>fr.denominator
            self.target_interval = 1 / self.target_fps

cdef class AudioWorker(FrameSyncWorker):
    """Worker used by :class:`FrameSyncThread` for audio frames
    """
    cdef AudioFrameSync audio_frame
    cdef size_t target_nsamples

    def __cinit__(self, *args, **kwargs):
        self.target_nsamples = 800

    cdef bint can_capture(self) except *:
        return self.frame_sync._audio_samples_available() >= self.target_nsamples

    cdef bint do_capture(self) except *:
        cdef size_t nsamp
        nsamp = self.frame_sync._capture_audio(self.target_nsamples, limit=True, truncate=False)
        return nsamp > 0

    cdef bint has_frame(self) except *:
        if self.audio_frame is not None:
            return True
        if self.frame_sync.audio_frame is not None:
            self.audio_frame = self.frame_sync.audio_frame
            return True
        return False

    @cython.cdivision(True)
    cdef void update_fps(self) except *:
        cdef VideoFrameSync video_frame = self.frame_sync.video_frame
        cdef frame_rate_t* fr
        cdef double fps
        cdef size_t fs = self.audio_frame._get_sample_rate()
        cdef size_t nsamp
        nsamp = self.target_nsamples
        fps = nsamp / <double>fs
        # if fs == 0:
        #     fps = 9
        #     nsamp = 1600
        # elif video_frame is None:
        #     nsamp = self.target_nsamples
        #     fps = nsamp / <double>fs
        # else:
        #     fr = video_frame._get_frame_rate()
        #     if fr.numerator == 0 or fr.denominator == 0:
        #         fps = 9
        #         nsamp = 1600
        #     else:
        #         fps = fr.numerator / <double>fr.denominator
        #         nsamp = lround((1 / fps) / (1 / <double>fs))
        #         fps = fs / nsamp
        self.target_nsamples = nsamp
        self.target_fps = fps
        self.target_interval = 1.0 / fps


class FrameSyncThread(threading.Thread):
    """A thread designed for use with :class:`FrameSync`

    This can be used to handle video and audio using two separate threads. One
    thread would be set to use :attr:`~ReceiveFrameType.recv_video` and the
    other to :attr:`~ReceiveFrameType.recv_audio`.

    Arguments:
        frame_sync (FrameSync): The FrameSync instance
        ft (ReceiveFrameType): The type(s) of frames to receive (either
            :attr:`~.receiver.ReceiveFrameType.recv_video` or
            :attr:`~.receiver.ReceiveFrameType.recv_audio`)

    Attributes:
        worker (FrameSyncWorker): Either a :class:`VideoWorker`
            or :class:`AudioWorker`

    """
    def __init__(self, FrameSync frame_sync, ReceiveFrameType ft):
        super().__init__()
        self.ft = ft
        self.stopped = threading.Event()
        if ft == ReceiveFrameType.recv_video:
            self.worker = VideoWorker(frame_sync)
        elif ft == ReceiveFrameType.recv_audio:
            self.worker = AudioWorker(frame_sync)
        else:
            raise ValueError('frame type must be `recv_video` or `recv_audio`')

    def run(self):
        cdef FrameSyncWorker w = self.worker
        try:
            w.run()
        except:
            import traceback
            traceback.print_exc()
        finally:
            self.stopped.set()

    def stop(self):
        """Stop the thread
        """
        cdef FrameSyncWorker w = self.worker
        w.stop()

    def set_callback(self, cb):
        """Set the callback
        """
        cdef FrameSyncWorker w = self.worker
        w.callback.set_callback(cb)

    def remove_callback(self):
        cdef FrameSyncWorker w = self.worker
        w.callback.remove_callback()
