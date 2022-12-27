import cv2
import threading

class VideoCamera():
    def __init__(self):
        self.video = cv2.VideoCapture(0)
        (self.grabbed, self.frame) = self.video.read()
        self.file_name = "camera.jpg"
        threading.Timer(0.1, self.update).start()

    def __del__(self):
        print("deleted")
        self.video.release()

    def get_frame(self):
        image = self.frame
        _, jpeg = cv2.imencode('.jpg', image)
        return jpeg.tobytes()

    def update(self):
        while True:
            try:
                (self.grabbed, self.frame) = self.video.read()
                cv2.imwrite(self.file_name, self.frame)
            except KeyboardInterrupt:
                print("KeyboardInterrupt")
                break
            

cam = VideoCamera()
