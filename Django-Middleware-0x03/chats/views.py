from django.shortcuts import render
from rest_framework import viewsets, status, filters
from .models import Message, User, Conversation, Profile
from .serializers import MessageSerializer, ConversationSerializer, UserSerializer, ProfileSerializer
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework_simplejwt.views import TokenObtainPairView
from .auth import CustomTokenPairSerializer
from .permissions import IsParticipantOfConversation
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from .filters import MessageFilter
from .pagination import MessagePagination




class MessageViewSet(viewsets.ModelViewSet):
  queryset = Message.objects.all().order_by("-sent_at", "-message_id")
  serializer_class = MessageSerializer
  permission_classes = [IsAuthenticated, IsParticipantOfConversation ]
  filterset_class = MessageFilter
  pagination_class = MessagePagination

  def get_queryset(self):
    conversation_id = self.kwargs.get('conversation_id')
    return Message.objects.filter(conversation__participants=self.request.user)
    

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

  def get_permissions(self):
    if self.action == 'create':
      return [AllowAny()]
    return super().get_permissions()
  
  def create(self, request, *args, **kwargs):
    serialized = self.get_serializer(data=request.data)
    serialized.is_valid(raise_exception=True)
    user = serialized.save()

    #Generate token
    refresh = RefreshToken.for_user(user)
    access_token = str(refresh.access_token)
    refresh_token = str(refresh)

    response_data = serialized.data
    response_data.update({
      "access": access_token,
      "refresh": refresh_token
    })

    header = self.get_success_headers(serialized.data)
    return Response(response_data, status=status.HTTP_201_CREATED)

class ProfileViewSet(viewsets.ModelViewSet):
  queryset = Profile.objects.all()
  serializer_class = ProfileSerializer
  permission_classes = [IsAuthenticated]

  def perform_create(self, serializer):
    serializer.save(user=self.request.user)
  
  def query_user(self):
    return Profile.objects.filter(user=self.request.user)


class CustomTokenPairView(TokenObtainPairView):
  serializer_class = CustomTokenPairSerializer
