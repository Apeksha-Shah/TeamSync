# TeamSync/asgi.py
import os
from django.core.asgi import get_asgi_application
from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
from django.urls import path
from TeamSync.consumers import CodeEditorConsumer

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'TeamSync.settings')

websocket_urlpatterns = [
    path('ws/editor/<str:project_code>/', CodeEditorConsumer.as_asgi()),
]

application = ProtocolTypeRouter({
  "http": get_asgi_application(),
  "websocket": AuthMiddlewareStack(
        URLRouter(
            websocket_urlpatterns
        )
    ),
})
