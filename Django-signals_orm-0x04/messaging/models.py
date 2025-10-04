#from django.db import models

# Create your models here.

# messaging_app/models.py
import uuid
from django.db import models
from django.conf import settings
#from chats.models import User
User = settings.AUTH_USER_MODEL

class Message(models.Model):
  id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
  sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name="messaging_sent_messages")
  receiver = models.ForeignKey(User, on_delete=models.CASCADE, related_name="messaging_received_messages")
  content = models.TextField()
  edited = models.BooleanField(default=False)
  timestamp = models.DateTimeField(auto_now_add=True)

  def __str__(self):
    return f"Message from {self.sender} to {self.receiver}"

# messaging_app/models.py
class Notification(models.Model):
  id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
  user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="notifications")
  message = models.ForeignKey(Message, on_delete=models.CASCADE, related_name="notifications")
  is_read = models.BooleanField(default=False)
  created_at = models.DateTimeField(auto_now_add=True)

  def __str__(self):
    return f"Notification for {self.user} about message {self.message.id}"

class MessageHistory(models.Model):
  id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
  message = models.ForeignKey(Message, on_delete=models.CASCADE, related_name="history")
  old_content = models.TextField()
  edited_by = models.ForeignKey(User, on_delete=models.CASCADE, editable=False)
  edited_at = models.DateTimeField(auto_now_add=True)

  def __str__(self):
    return f"History of message {self.message.id} at {self.edited_at}" 