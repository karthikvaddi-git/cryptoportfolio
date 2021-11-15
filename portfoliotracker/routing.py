from django.urls import path
from . import consumers

websocket_urlpatterns = [
    path('ws/check/', consumers.ChatConsumer.as_asgi()),
]