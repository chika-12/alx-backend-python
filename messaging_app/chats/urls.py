from django.urls import path, include
from rest_framework import routers
from .views import MessageViewSet, ConversationViewSet, UserViewSet
from rest_framework_nested.routers import NestedDefaultRouter

router = routers.DefaultRouter()
router.register(r'messages', MessageViewSet, basename='message')
router.register(r'conversations', ConversationViewSet, basename='conversation')
router.register(r'users', UserViewSet, basename='user')

urlpatterns = [
    path('', include(router.urls)),
]