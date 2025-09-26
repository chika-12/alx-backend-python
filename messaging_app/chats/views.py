from django.shortcuts import render
from rest_framework import viewsets, status, filters
from .models import Message, User, Conversation
from .serializers import MessageSerializer, ConversationSerializer, UserSerializer
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework_simplejwt.views import TokenObtainPairView
from .auth import CustomTokenPairSerializer
from .permissions import IsParticipantOfConversation
from rest_framework.response import Response


class MessageViewSet(viewsets.ModelViewSet):
  queryset = Message.objects.all()
  serializer_class = MessageSerializer
  permission_classes = [IsAuthenticated, IsParticipantOfConversation ]
  def get_queryset(self):
    conversation_id = self.kwargs.get('conversation_id')
    return Message.objects.filter(conversation_id=conversation_id, conversation__participants=self.request.user)
    

class ConversationViewSet(viewsets.ModelViewSet):
  queryset = Conversation.objects.all()
  serializer_class = ConversationSerializer
  permission_classes = [IsAuthenticated, IsParticipantOfConversation ]


  def get_queryset(self):
    conversation_id = self.kwargs.get('conversation_id')
    return Message.objects.filter(conversation_id=conversation_id, conversation__participants=self.request.user)
  
  def create(self, request, *args, **kwargs):
    conversation_id = self.kwargs.get('conversation_id')
    conversation = Conversation.objects.get('conversation_id=conversation_id')

    if request.user not in conversation.participants.all():
      return Response({"detail": "Forbidedn"}, status=status.HTTP_403_FORBIDDEN)
    serializer = self.get_serializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    serializer.save(sender=request.user, conversation=conversation)
    return Response(serializer.data, status=status.HTTP_201_CREATED)
  

class UserViewSet(viewsets.ModelViewSet):
  queryset = User.objects.all()
  serializer_class = UserSerializer
  permission_classes = [IsAuthenticated]

class CustomTokenPairView(TokenObtainPairView):
  serializer_class = CustomTokenPairSerializer
