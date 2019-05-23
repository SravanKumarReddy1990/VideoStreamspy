from time import time


class Camera(object):
    """An emulated camera implementation that streams a repeated sequence of
    files 1.jpg, 2.jpg and 3.jpg at a rate of one frame per second."""

    def __init__(self):
       self.frames = []

    def get_frame(self):
        vidcap = cv2.VideoCapture('VID-20190112-WA0003.mp4')
        success,image = vidcap.read()
        count = 0
        success = True
        while success:
            self.frames(image)
            #cv2.imwrite("frame%d.jpg" % count, image)     
            # save frame as JPEG file
            success,image = vidcap.read()
            print('Read a new frame: ', success)
            count += 1
        return self.frames[int(time()) % count]
