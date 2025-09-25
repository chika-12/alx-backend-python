from django.shortcuts import render
from rest_framework import viewsets, status, filters
from .models import Message, User, Conversation
from .serializers import MessageSerializer, ConversationSerializer, UserSerializer
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework_simplejwt.views import TokenObtainPairView
from .auth import CustomTokenPairSerializer
from .permissions import IsOwnerOrParticipant


class MessageViewSet(viewsets.ModelViewSet):
  queryset = Message.objects.all()
  serializer_class = MessageSerializer
  permission_classes = [IsAuthenticated, IsOwnerOrParticipant]

class ConversationViewSet(viewsets.ModelViewSet):
  queryset = Conversation.objects.all()
  serializer_class = ConversationSerializer
  permission_classes = [IsAuthenticated, IsOwnerOrParticipant]

class UserViewSet(viewsets.ModelViewSet):
  queryset = User.objects.all()
  serializer_class = UserSerializer
  permission_classes = [IsAuthenticated]

class CustomTokenPairView(TokenObtainPairView):
  serializer_class = CustomTokenPairSerializer
