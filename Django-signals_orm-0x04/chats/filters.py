import django_filters
from .models import Message

class MessageFilter(django_filters.FilterSet):
  sender = django_filters.NumberFilter(field_name='sender', lookup_expr='exact')
  message_id = django_filters.NumberFilter(field_name='message_id', lookup_expr='exact')
  conversation = django_filters.NumberFilter(field_name='conversation', lookup_expr='exact')
  sent_at = django_filters.DateTimeFilter(field_name='sent_at', lookup_expr='exact')

  class Meta():
    model = Message
    fields = ['sender', 'message_id', 'conversation', 'sent_at']