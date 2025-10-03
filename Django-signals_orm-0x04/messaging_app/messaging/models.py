from django.db import models
from django.conf import settings

User = settings.AUTH_USER_MODEL
# Create your models here.

class Message(models.Model):
  sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name="sent_message")
  receiver = models.ForeignKey(User, on_delete=models.CASCADE, related_name="received_message")
  content = models.TextField()
  timestamp = models.DateTimeField(auto_created=True)
  def __str__(self):
    return f"message from {self.sender} to {self.receiver}"
  
class Notification(models.Model):
  user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="notifications")
  message = models.ForeignKey(Message, on_delete=models.CASCADE, related_name="notifications")
  is_read = models.BooleanField(default=False)
  created_at = models.DateTimeField(auto_now_add=True)
  def __str__(self):
    return f"Notification for {self.user} about message {self.message.id}"
