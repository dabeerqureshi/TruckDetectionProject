import cv2
import numpy as np

def compare_frames(frame, reference_image):
    """ Compare the current frame with the reference image. """
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    gray_reference = cv2.cvtColor(reference_image, cv2.COLOR_BGR2GRAY)
    diff = cv2.absdiff(gray_frame, gray_reference)
    _, thresh = cv2.threshold(diff, 25, 255, cv2.THRESH_BINARY)
    change_score = np.sum(thresh) / (frame.shape[0] * frame.shape[1] * 255)
    return change_score > 0.1  # Example threshold value
