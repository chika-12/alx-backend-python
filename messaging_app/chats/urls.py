from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import MessageViewSet, ConversationViewSet, UserViewSet

routers = DefaultRouter()
routers.register(r'messages', MessageViewSet, basename='message')
routers.register(r'conversations', ConversationViewSet, basename='conversation')
routers.register(r'users', UserViewSet, basename='user')

urlpatterns = [
    path('', include(routers.urls)),
]