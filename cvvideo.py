import tkinter as tk
import cv2



class VideoCapture:
    def __init__(self):
        self.video = cv2.VideoCapture(0)
        self.video.set(3, 400) #width (change second val)
        self.video.set(4, 400) #height (change second val)
        if not self.video.isOpened():
            raise Exception("Camera Not Found")

    def get_frame(self):
        success, frame = self.video.read()
        if success:
            return success, frame

    def __del__(self):
        if self.video.isOpened():
            self.video.release()