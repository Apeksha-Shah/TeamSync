# TeamSync/routing.py
from django.urls import path
from .consumers import CodeEditorConsumer

websocket_urlpatterns = [
    path('ws/editor/<str:project_code>/', CodeEditorConsumer.as_asgi()),
]
