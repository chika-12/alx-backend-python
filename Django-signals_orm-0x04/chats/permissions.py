from rest_framework import permissions


class IsParticipantOfConversation(permissions.BasePermission):
  """
    Allow access only if the user is a participant in the conversation
    or the sender/recipient of the message.
  """
  def has_object_permission(self, request, view, obj):

    if not request.user.is_authenticated:
      return False
    
    if request.method in permissions.SAFE_METHODS:
      return request.user in obj.conversation.participants.all()
    elif request.method in ["PUT", "PATCH", "DELETE"]:
      return request.user == obj.sender
    else:
      return False
  