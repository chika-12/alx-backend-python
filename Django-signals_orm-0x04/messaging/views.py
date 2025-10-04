from django.shortcuts import render

# Create your views here.
from .serializers import MessageHistorySerializers
from rest_framework import viewsets
from .models import MessageHistory

class MessageHistoryViewsets(viewsets.ReadOnlyModelViewSet):
  serializer_class = MessageHistorySerializers
  def queryset(self):
    message_id = self.kwargs.get("id")
    return MessageHistory.objects.filter(id=message_id).order_by("-edited_at")
