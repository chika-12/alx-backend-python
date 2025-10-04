from django.shortcuts import render

# Create your views here.
from .serializers import MessageHistorySerializers, MessageSerializer
from rest_framework import viewsets, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .models import MessageHistory, Message
from chats.models import User
#from chats.serializers import UserSerializer
from rest_framework.decorators import api_view, permission_classes
from utils import get_replies_recursive

class MessageHistoryViewsets(viewsets.ReadOnlyModelViewSet):
  serializer_class = MessageHistorySerializers
  def queryset(self):
    message_id = self.kwargs.get("id")
    return MessageHistory.objects.filter(id=message_id).order_by("-edited_at")
  
@api_view('DELETE')
@permission_classes(IsAuthenticated)
def delete_user(request):
  user = request.user
  user.delete()
  return Response({"message": "Your account has been successfully deactivated."},
        status=status.HTTP_204_NO_CONTENT)

class MessageViewSet(viewsets.ModelViewSet):
  serializer_class = MessageSerializer

  def get_queryset(self):
    return (
      Message.objects
      .select_related("sender", "receiver", "parent_message")
      .prefetch_related("replies") 
      .order_by("-timestamp")
    )

@api_view(["GET"])
def message_thread(request, message_id):
  message = Message.objects.select_related('sender', 'reciever').get(id=message_id)
  data = {
    'id' :message.id,
    'content': message.content,
    'sender' :message.sender.username,
    'replies' :get_replies_recursive(message)
  }
  return Response(data)
