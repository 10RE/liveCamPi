import cv2
import threading

class VideoCamera(object):
    def __init__(self):
        self.video = cv2.VideoCapture(-1)
        (self.grabbed, self.frame) = self.video.read()
        self.file_name = "camera.jpg"
        threading.Thread(target=self.update, args=()).start()
        threading.Thread(target=self.save, args=()).start()

    def __del__(self):
        print("deleted")
        self.video.release()

    def get_frame(self):
        image = self.frame
        _, jpeg = cv2.imencode('.jpg', image)
        return jpeg.tobytes()

    def update(self):
        while True:
            (self.grabbed, self.frame) = self.video.read()

    def save(self):
        while True:
            cv2.imwrite(self.file_name, self.frame)

cam = VideoCamera()
