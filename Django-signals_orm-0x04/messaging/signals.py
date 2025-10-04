from django.db.models.signals import post_save, pre_save, post_delete
from django.dispatch import receiver
from .models import Message, Notification, MessageHistory
from chats.models import User

@receiver(post_save, sender=Message)
def create_notification(sender, instance, create, **kwargs):
  if create:
    Notification.objects.create(user=instance.receiver, message=instance)

@receiver(pre_save, sender=Message)
def logg_message_edit(sender, instance, **kwargs):
  if instance.id:
    old_message = Message.objects.get(id=instance.id)
    if old_message.content != instance.content:
      MessageHistory.objects.create(
        message=instance,
        edited_by=instance.sender,
        old_content=old_message.content
      )
      instance.edited=True

@receiver(post_delete, sender=User)
def delete_user_related_data(sender, instance, **kwargs):
  """
  Deletes all messages, notifications, and message histories 
  linked to the deleted user.
  """
  Message.objects.filter(sender=instance).delete()
  Message.objects.filter(receiver=instance).delete()
  Notification.objects.filter(user=instance).delete()
  MessageHistory.objects.filter(edited_by=instance).delete()

  print(f"🗑️ All data for user '{instance}' has been cleaned up.")