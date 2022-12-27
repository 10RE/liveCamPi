from django.conf import settings
from django.shortcuts import get_object_or_404, render, redirect
from django.http import Http404, StreamingHttpResponse, HttpResponse
from .models import Camera
import cv2
import threading

# Create your views here.
def index(request):
    #camera = Camera()
    #camera.image.save()
    #image = get_object_or_404(Camera, pk=1)
    #context = {
    #    'image': image
    #}
    image_data = open("/home/10RE/camera.jpg", mode='r').read()
    return HttpResponse(image_data, content_type="image/png")
    #return render(request, 'liveCamPi/index.html', context)
    #cam = VideoCamera()
    #return StreamingHttpResponse(gen(cam), content_type="multipart/x-mixed-replace;boundary=frame")
    #if request.user.is_authenticated:
    #    return StreamingHttpResponse(gen(cam), content_type="multipart/x-mixed-replace;boundary=frame")
    #else:
    #    return redirect(f'{settings.LOGIN_URL}?next={request.path}')

