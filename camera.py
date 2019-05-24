from time import time
import cv2


class Camera(object):
    """An emulated camera implementation that streams a repeated sequence of
    files 1.jpg, 2.jpg and 3.jpg at a rate of one frame per second."""

    def __init__(self):
       self.video = cv2.VideoCapture('VID-20190112-WA0003.mp4')

    def __del__(self):
        self.video.release()

    def get_frame(self):
        success,image = self.video.read()
        ret, jpeg = cv2.imencode('.jpg', image)
        return jpeg.tobytes()
