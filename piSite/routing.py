from django.urls import re_path

from liveCamPi import consumers

websocket_urlpatterns = [
    re_path(r'video/(?P<v_name>\w+)/$', consumers.Consumer.as_asgi()),
] 