def get_replies_recursive(message):
  replies = message.replies.all().select_related('sender', 'receiver')
  data = []
  for reply in replies:
    data.append({
      "id": reply.id,
      "content": reply.content,
      "sender": reply.sender.username,
      "replies": get_replies_recursive(reply)
    })
    return data
