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
from django.db.models.signals import post_save
from django.dispatch import receiver




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
    return Conversation.objects.filter(participants=self.request.user)
  
  def create(self, request, *args, **kwargs):
    participant_id = request.data.get("participants", [])

    if request.user.user_id not in participant_id:
      participant_id.append(request.user.user_id)

    conversation = Conversation.objects.create()
    conversation.participants.set(User.objects.filter(user_id__in=participant_id))
    serializer = self.get_serializer(conversation)
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
  serializer_class = ProfileSerializer
  permission_classes = [IsAuthenticated]
  def get_queryset(self):
    # Only return the profile for the logged-in user
    return Profile.objects.filter(user=self.request.user)
  def perform_create(self, serializer):
    # Always attach profile to logged-in user
    serializer.save(user=self.request.user)


class CustomTokenPairView(TokenObtainPairView):
  serializer_class = CustomTokenPairSerializer

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
  if created:
    Profile.objects.create(user=instance)
