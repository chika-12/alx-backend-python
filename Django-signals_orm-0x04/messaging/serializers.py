from .models import MessageHistory, Message
from rest_framework import serializers

class MessageHistorySerializers(serializers.ModelSerializer):
  edited_by = serializers.StringRelatedField() 

  class Meta:
    model = MessageHistory
    fields = ["old_content", "edited_at", "edited_by", "message"]

class MessageSerializer(serializers.ModelSerializer):
  replies = serializers.StringRelatedField(many=True, read_only=True)

  class Meta:
    model = Message
    fields = ["id", "sender", "receiver", "content", "timestamp", "parent_message", "replies"]
