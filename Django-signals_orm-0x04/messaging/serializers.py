from .models import MessageHistory
from rest_framework import serializers

class MessageHistorySerializers(serializers.ModelSerializer):
  edited_by = serializers.StringRelatedField() 

  class Meta:
    model = MessageHistory
    fields = ["old_content", "edited_at", "edited_by", "message"]