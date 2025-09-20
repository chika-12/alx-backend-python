from rest_framework import serializers
from .models import User, Conversation, Message

class UserSerializer(serializers.ModelSerializer):
  class Meta:
    model = User
    fields = ['user_id', 'first_name', 'last_name', 'email', 'role']

class MessageSerializer(serializers.ModelSerializer):
  class Meta:
    fields = ['message_id', 'sender', 'message_body', 'sent_at']

class ConversationSerializers(serializers.ModelSerilizers):
  participants = UserSerializer(many=True, read_only=True)
  messages = MessageSerializer(many=True, read_only=True)  
  class Meta:
    fields = ['conversation_id', 'participants', 'messages', 'created_at']
