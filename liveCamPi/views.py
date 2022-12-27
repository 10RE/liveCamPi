from django.conf import settings
from django.shortcuts import get_object_or_404, render, redirect
from django.http import Http404, StreamingHttpResponse, HttpResponse
from .models import Camera
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

def gen(camera):
    while True:
        frame = camera.get_frame()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')

def v_name(request, v_name):
	return render(request, 'liveCamPi/cam.html', {
		'v_name': v_name
	})

# Create your views here.
def index(request):
    #camera = Camera()
    #camera.image.save()
    #image = get_object_or_404(Camera, pk=1)
    #context = {
    #    'image': image
    #}
    #return render(request, 'liveCamPi/cam.html', {})
    #image_data = open("camera.jpg", mode='rb').read()
    #return HttpResponse(image_data, content_type="image/png")
    #return render(request, 'liveCamPi/index.html', context)
    cam = VideoCamera()
    #return StreamingHttpResponse(gen(cam), content_type="multipart/x-mixed-replace;boundary=frame")
    if request.user.is_authenticated:
       return StreamingHttpResponse(gen(cam), content_type="multipart/x-mixed-replace;boundary=frame")
    else:
       return redirect(f'{settings.LOGIN_URL}?next={request.path}')

