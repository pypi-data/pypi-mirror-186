import cv2
import numpy as np
from tqdm import tqdm


class BackgroundEstimation:
    def __init__(self, video_file_name: str, frame_fraction: float = 0.5):

        self.cap = cv2.VideoCapture(video_file_name)
        self.num_frames = self.cap.get(cv2.CAP_PROP_FRAME_COUNT)
        self.frame_fraction = frame_fraction
        self.frame_fraction_num = int(self.num_frames * self.frame_fraction)

    def _mean_estimate(self, selected_frames):
        """
        Given selected frames, estimate mean value for each pixels and return the resulting image
        """
        mean_frame = np.mean(selected_frames, axis=0).astype(dtype=np.uint8)
        return mean_frame

    def _median_estimate(self, selected_frames):
        """
        Given selected frames, estimate median value for each pixels and return the resulting image
        """
        median_frame = np.median(selected_frames, axis=0).astype(dtype=np.uint8)
        return median_frame

    def _select_frames(self):
        """
        For the provided video select and return n number of frames based on frame_fraction_num
        """
        frame_ids = self.num_frames * np.random.uniform(size=self.frame_fraction_num)

        # Store selected frames in an array
        selected_frames = []
        for fid in tqdm(frame_ids):
            self.cap.set(cv2.CAP_PROP_POS_FRAMES, fid)
            ret, frame = self.cap.read()
            selected_frames.append(frame)

        return selected_frames

    def _cleanup(self):
        """
        Release video reader
        """
        self.cap.release()

    def get_background(self, method: str = "median"):
        """
        Given the background estimation method select frames and return the background image
        """
        selected_frames = self._select_frames()

        if method == "mean":
            result_image = self._mean_estimate(selected_frames)

        elif method == "median":
            result_image = self._median_estimate(selected_frames)

        else:

            result_image = None

        self._cleanup()

        return result_image
