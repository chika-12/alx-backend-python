from django.contrib import admin

# Register your models here.
# messaging_app/admin.py
from django.contrib import admin
from .models import Message, Notification, MessageHistory

@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
  list_display = ('id', 'sender', 'receiver', 'timestamp')
  search_fields = ('sender__username', 'receiver__username', 'content')

@admin.register(Notification)
class NotificationAdmin(admin.ModelAdmin):
  list_display = ('id', 'user', 'message', 'is_read', 'created_at')
  list_filter = ('is_read', 'created_at')

@admin.register(MessageHistory)
class MessageHistoryAdmin(admin.ModelAdmin):
  list_display = ('id', 'message', 'old_content', 'edited_at')