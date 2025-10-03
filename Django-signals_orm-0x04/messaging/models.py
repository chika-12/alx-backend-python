#from django.db import models

# Create your models here.

# messaging_app/models.py
import uuid
from django.db import models
from django.conf import settings
from chats.models import User

class Message(models.Model):
  sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name="sent_messages")
  receiver = models.ForeignKey(User, on_delete=models.CASCADE, related_name="received_messages")
  content = models.TextField()
  timestamp = models.DateTimeField(auto_now_add=True)

  def __str__(self):
    return f"Message from {self.sender} to {self.receiver}"

# messaging_app/models.py
class Notification(models.Model):
  user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="notifications")
  message = models.ForeignKey(Message, on_delete=models.CASCADE, related_name="notifications")
  is_read = models.BooleanField(default=False)
  created_at = models.DateTimeField(auto_now_add=True)

  def __str__(self):
    return f"Notification for {self.user} about message {self.message.id}"
