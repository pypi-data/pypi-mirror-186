import numpy as np
import cv2
from tqdm import tqdm

class BackgroundEstimation:
    def __init__(self, video_file_name:str, frame_fraction:float = 0.5):

        self.cap = cv2.VideoCapture(video_file_name)
        self.num_frames = self.cap.get(cv2.CAP_PROP_FRAME_COUNT)
        self.frame_fraction = frame_fraction
        self.frame_fraction_num = int(self.num_frames * self.frame_fraction)
    
    def _mean_image(self, selected_frames):
        mean_frame = np.mean(selected_frames, axis=0).astype(dtype=np.uint8)
        return mean_frame

    def _median_image(self, selected_frames):
        median_frame = np.median(selected_frames, axis=0).astype(dtype=np.uint8)
        return median_frame
    
    def _select_frames(self):

        # Randomly select n frames
        frame_ids = self.num_frames * np.random.uniform(size = self.frame_fraction_num)

        # Store selected frames in an array
        selected_frames = []
        for fid in tqdm(frame_ids):
            self.cap.set(cv2.CAP_PROP_POS_FRAMES, fid)
            ret, frame = self.cap.read()
            selected_frames.append(frame)

        return selected_frames
    
    def _cleanup(self):
        self.cap.release()

    def get_background(self, method:str = "median"):

        selected_frames = self._select_frames()

        if method == "mean":
            result_image = self._mean_image(selected_frames)

        elif method == "median":
            result_image = self._mean_image(selected_frames)

        else:

            result_image = None

        self._cleanup()

        return result_image

