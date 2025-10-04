from django.shortcuts import render

# Create your views here.
from .serializers import MessageHistorySerializers
from rest_framework import viewsets, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .models import MessageHistory
from chats.models import User
from chats.serializers import UserSerializer
from rest_framework.decorators import api_view, permission_classes

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