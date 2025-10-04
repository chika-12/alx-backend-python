from django.shortcuts import render

# Create your views here.
from .serializers import MessageHistorySerializers
from rest_framework import viewsets, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .models import MessageHistory
from chats.models import User
from chats.serializers import UserSerializer

class MessageHistoryViewsets(viewsets.ReadOnlyModelViewSet):
  serializer_class = MessageHistorySerializers
  def queryset(self):
    message_id = self.kwargs.get("id")
    return MessageHistory.objects.filter(id=message_id).order_by("-edited_at")
  
class deleteUser(viewsets.ModelViewSet):
  queryset = User.objects.all()
  serializer_class = UserSerializer
  permission_classes = [IsAuthenticated]

  def destroy(self, request):
    user = self.get_object()
    if request.user != user:
      return Response({"error": "You can not delete this account"}, status=status.HTTP_403_FORBIDDEN)
    
    user.soft_delete()
    return Response({"error": "Your account has been successfully deactivated"}, status=status.HTTP_204_NO_CONTENT)
