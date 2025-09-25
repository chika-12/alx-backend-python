from rest_framework.permissions import BasePermission


class IsOwnerOrParticipant(BasePermission):
  """
    Allow access only if the user is a participant in the conversation
    or the sender/recipient of the message.
  """
  def has_object_permission(self, request, view, obj):
    if request.user == obj.sender:
      return True
    elif request.user in obj.conversation.participants.all():
      return True
    else:
      return False
  