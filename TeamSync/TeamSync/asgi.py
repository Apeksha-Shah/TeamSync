# TeamSync/asgi.py
import os
from django.core.asgi import get_asgi_application
from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
from django.urls import path
from TeamSync.consumers import CodeEditorConsumer
import TeamSync.routing as routing

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'TeamSync.settings')


application = ProtocolTypeRouter({
  "http": get_asgi_application(),
  "websocket": AuthMiddlewareStack(
        URLRouter(
            routing.websocket_urlpatterns
        )
    ),
})
