import time
from collections import deque, namedtuple

import cv2
import numpy as np
from scipy.signal import savgol_filter


class KalmanFilter:
    """A kalman filter for 2D/3D points"""

    def __init__(
        self, joints_dim=3, num_joints=21, cov_process=0.002, cov_measure=0.01
    ):

        # Check input dimension
        self.num_joints = num_joints
        self.joints_dim = joints_dim
        input_dim = self.joints_dim * self.num_joints
        assert num_joints == 21, "only 21 points allowed"

        # Set up process and input dimensions
        self.state_num = 2 * input_dim
        self.measure_num = input_dim

        # initiate filter from opencv
        # No control parameter for now
        self.filter = cv2.KalmanFilter(self.state_num, self.measure_num, 0)

        # Store the initial state
        self.state = np.zeros((self.state_num, 1), np.float32)
        if joints_dim == 3:
            self.state[: self.measure_num, :] = np.array([320, 256, 0] * num_joints)[
                :, np.newaxis
            ]
        elif joints_dim == 2:
            self.state[: self.measure_num, :] = np.array([320, 256] * num_joints)[
                :, np.newaxis
            ]

        self.filter.statePost = self.state
        # initialize the measurements with 0s
        self.measurement = np.zeros((self.measure_num, 1), np.float32)

        # initialize the prediction results with 0s
        self.prediction = np.zeros((self.state_num, 1), np.float32)

        # Kalman filter parameters setup for 2D
        self.filter.transitionMatrix = np.eye(
            self.state_num, k=self.state_num // 2, dtype=np.float32
        )
        self.filter.transitionMatrix[
            np.diag_indices_from(self.filter.transitionMatrix)
        ] = 1.0
        self.filter.measurementMatrix = np.eye(
            self.measure_num, self.state_num, dtype=np.float32
        )

        self.filter.processNoiseCov = (
            np.eye(self.state_num, dtype=np.float32) * cov_process
        )
        self.filter.measurementNoiseCov = (
            np.eye(self.measure_num, dtype=np.float32) * cov_measure
        )

    def update(self, measurement):
        """update the kalman filter, containing both prediction by previous results, and the
        correction with new measurements. Results are stored in the self.state.
        Input: measurement --- the new measurement to update kalman filter"""
        # make prediction based on previous results with kalman filter
        self.prediction = self.filter.predict()

        # Get new measurements
        self.measurement = measurement.reshape(-1, 1)

        # correct according to measurement
        self.filter.correct(self.measurement)

        # update the state value
        self.state = self.filter.statePost

        # get the state of the kalman filter
        return self.state[: self.measure_num, :].reshape(-1, self.joints_dim)

    def predict(self):
        # make prediction based on previous results with kalman filter
        self.prediction = self.filter.predict()
        self.state = self.prediction
        # return the prediction results
        return self.state

    def correct(self, measurement):
        # Correct the prediciton with new measurements
        self.measurement = measurement.reshape(-1, 1)

        # correct according to measurement
        self.filter.correct(self.measurement)
        # update the state value
        self.state = self.filter.statePost

        # return corrected results
        return self.state


class LowPassFilter:
    def __init__(self, alpha=1.0):
        self.alpha = alpha
        self.initialized = False

    def apply(self, value):
        # Note that value can be a scalar or a numpy array
        if self.initialized:
            v = self.alpha * value + (1.0 - self.alpha) * self.stored_value
        else:
            v = value
            self.initialized = True
        self.stored_value = v
        return v

    def apply_with_alpha(self, value, alpha):
        self.alpha = alpha
        return self.apply(value)


class OneEuroFilter:
    def __init__(self, x0, dx0=0.0, min_cutoff=1.7, beta=0.3, d_cutoff=30.0, fps=None):
        """One Euro Filter for keypoints smoothing.
        Args:
            x0 (np.ndarray[K, 2]): Initialize keypoints value
            dx0 (float): 0.0
            min_cutoff (float): parameter for one euro filter
            beta (float): parameter for one euro filter
            d_cutoff (float): Input data FPS
            fps (float): Video FPS for video inference
        """

        # The parameters.
        self.data_shape = x0.shape
        self.min_cutoff = np.full(x0.shape, min_cutoff)
        self.beta = np.full(x0.shape, beta)
        self.d_cutoff = np.full(x0.shape, d_cutoff)
        # Previous values.
        self.x_prev = x0.astype(np.float32)
        self.dx_prev = np.full(x0.shape, dx0)
        self.mask_prev = np.ma.masked_where(x0 <= 0, x0)
        self.realtime = True
        if fps is None:
            # Using in realtime inference
            self.t_e = None
            self.skip_frame_factor = d_cutoff
        else:
            # fps using video inference
            self.realtime = False
            self.d_cutoff = np.full(x0.shape, float(fps))
        self.t_prev = time.time()

    def smoothing_factor(self, t_e, cutoff):
        r = 2 * np.pi * cutoff * t_e
        return r / (r + 1)

    def exponential_smoothing(self, a, x, x_prev):
        return a * x + (1 - a) * x_prev

    def update(self, x, t_e=1.0):
        """Compute the filtered signal.
        parameter (cutoff, beta) from VNect
        (http://gvv.mpi-inf.mpg.de/projects/VNect/)
        Realtime Camera fps (d_cutoff) default 30.0
        Args:
            x (np.ndarray[K, 2]): keypoints results in frame
            t_e (Optional): video skip frame count for posetrack
                evaluation
        """
        assert x.shape == self.data_shape

        t = 0
        if self.realtime:
            t = time.time()
            t_e = (t - self.t_prev) * self.skip_frame_factor
        t_e = np.full(x.shape, t_e)
        # missing keypoints mask
        mask = np.ma.masked_where(x <= 0, x)

        # The filtered derivative of the signal.
        a_d = self.smoothing_factor(t_e, self.d_cutoff)
        dx = (x - self.x_prev) / t_e
        dx_hat = self.exponential_smoothing(a_d, dx, self.dx_prev)

        # The filtered signal.
        cutoff = self.min_cutoff + self.beta * np.abs(dx_hat)
        a = self.smoothing_factor(t_e, cutoff)
        self.x_hat = self.exponential_smoothing(a, x, self.x_prev)

        # missing keypoints remove
        np.copyto(self.x_hat, -10, where=mask.mask)

        # Memorize the previous values.
        self.x_prev = self.x_hat
        self.dx_prev = dx_hat
        self.t_prev = t
        self.mask_prev = mask

        return self.x_hat


class RelativeVelocityFilter:
    def __init__(self, window_size=5, velocity_scale=10, shape=1):
        self.window_size = window_size
        self.velocity_scale = velocity_scale
        self.last_value = np.zeros(shape)
        self.last_value_scale = np.ones(shape)
        self.last_timestamp = -1
        self.window = deque(maxlen=self.window_size)
        self.WindowElement = namedtuple("WindowElement", ["distance", "duration"])
        self.lpf = LowPassFilter()

    def get_object_scale(self, landmarks):
        lm_min = np.min(landmarks[:2], axis=1)  # min x , min y
        lm_max = np.max(landmarks[:2], axis=1)  # max x , max y
        return np.mean(lm_max - lm_min)  # average of object width and object height

    def update(self, value, timestamp=None):
        # Applies filter to the value.
        # timestamp - timestamp associated with the value (for instance,
        #             timestamp of the frame where you got value from)
        # value_scale - value scale (for instance, if your value is a distance
        #               detected on a frame, it can look same on different
        #               devices but have quite different absolute values due
        #               to different resolution, you should come up with an
        #               appropriate parameter for your particular use case)
        # value - value to filter
        value_scale = 1 / self.get_object_scale(value)
        if timestamp is None:
            timestamp = time.perf_counter()
        if self.last_timestamp == -1:
            alpha = 1.0
        else:
            distance = value * value_scale - self.last_value * self.last_value_scale
            duration = timestamp - self.last_timestamp
            cumul_distance = distance.copy()
            cumul_duration = duration
            # Define max cumulative duration assuming
            # 30 frames per second is a good frame rate, so assuming 30 values
            # per second or 1 / 30 of a second is a good duration per window element
            max_cumul_duration = (1 + len(self.window)) * 1 / 30
            for el in self.window:
                if cumul_duration + el.duration > max_cumul_duration:
                    break
                cumul_distance += el.distance
                cumul_duration += el.duration
            velocity = cumul_distance / cumul_duration
            alpha = 1 - 1 / (1 + self.velocity_scale * np.abs(velocity))
            self.window.append(self.WindowElement(distance, duration))

        self.last_value = value
        self.last_value_scale = value_scale
        self.last_timestamp = timestamp
        self.value_fi = self.lpf.apply_with_alpha(value, alpha)

        return self.value_fi


class SavgolFilter:
    def __init__(self, queue_len=6, poly_order=3):
        self.queue_len = queue_len
        self.win_size = queue_len - 1 if queue_len % 2 == 0 else queue_len - 2
        self.poly_order = poly_order
        self.kpt_queue = deque(maxlen=queue_len)

    def update(self, x):
        self.kpt_queue.append(x)
        if len(self.kpt_queue) < self.queue_len:
            self.x_hat = x
        else:
            transKpts = np.array(self.kpt_queue).transpose(1, 2, 0)
            result = savgol_filter(transKpts, self.win_size, self.poly_order).transpose(
                2, 0, 1
            )
            self.x_hat = result[-1, :, :]
        return self.x_hat
