from rest_framework import serializers
from .models import User, Conversation, Message


# -------------------------------
# User Serializer
# -------------------------------
class UserSerializer(serializers.ModelSerializer):
    role = serializers.CharField(max_length=10, required=False)

    class Meta:
        model = User
        fields = ['user_id', 'username', 'first_name', 'last_name', 'email', 'role', 'password']
        extra_kwargs = {
            'password': {'write_only': True}
        }
    
    def create(self, validated_data):
        password = validated_data.pop("password")
        user = User(**validated_data)
        user.set_password(password)
        user.save()
        return user

    def validate_role(self, value):
        if value not in ['guest', 'host', 'admin']:
            raise serializers.ValidationError("Role must be guest, host, or admin")
        return value

# -------------------------------
# Message Serializer
# -------------------------------
class MessageSerializer(serializers.ModelSerializer):
    sender_name = serializers.SerializerMethodField()  # dynamic field

    class Meta:
        model = Message
        fields = ['message_id', 'sender', 'sender_name', 'message_body', 'sent_at']

    def get_sender_name(self, obj):
        return f"{obj.sender.first_name} {obj.sender.last_name}"

# -------------------------------
# Conversation Serializer
# -------------------------------
class ConversationSerializer(serializers.ModelSerializer):
    participants = UserSerializer(many=True)
    messages = MessageSerializer(many=True, read_only=True)
    total_messages = serializers.SerializerMethodField()

    class Meta:
        model = Conversation
        fields = ['conversation_id', 'participants', 'messages', 'total_messages', 'created_at']

    def get_total_messages(self, obj):
        return obj.messages.count()


