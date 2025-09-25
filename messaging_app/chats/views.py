from django.shortcuts import render

# Create your views here.

from rest_framework import viewsets, status, filters
from .models import Message, User, Conversation
from .serializers import MessageSerializer, ConversationSerializer, UserSerializer
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.views import TokenObtainPairView
from .auth import CustomTokenPairSerializer

class MessageViewSet(viewsets.ModelViewSet):
  queryset = Message.objects.all()
  serializer_class = MessageSerializer
  permission_classes = [AllowAny]

class ConversationViewSet(viewsets.ModelViewSet):
  queryset = Conversation.objects.all()
  serializer_class = ConversationSerializer
  permission_classes = [AllowAny]

class UserViewSet(viewsets.ModelViewSet):
  queryset = User.objects.all()
  serializer_class = UserSerializer
  permission_classes = [AllowAny]

class CustomTokenPairView(TokenObtainPairView):
  serializer_class = CustomTokenPairSerializer
