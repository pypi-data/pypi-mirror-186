from channels.routing import ProtocolTypeRouter, URLRouter
from channels.security.websocket import AllowedHostsOriginValidator
from channels.auth import AuthMiddlewareStack
from django.urls import path
from app.consumers import ChatConsumer
from .asgi import application_app

application = ProtocolTypeRouter({
    # Empty for now (http->django views is added by default)
    "http": application_app,
    'websocket': AllowedHostsOriginValidator(
        AuthMiddlewareStack(
            URLRouter(
                [
                    path('ws/run/', ChatConsumer.as_asgi()),
                ]
            )
        )
    )
})