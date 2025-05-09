from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer


def send_notification(notification_type, content):
    channel = get_channel_layer()
    async_to_sync(channel.group_send)(
        "notification",
        {
            "type": "send_notification",
            "message": {"content": content, "type": notification_type},
        },
    )

def send_chat_message(message):
    channel = get_channel_layer()
    async_to_sync(channel.group_send)(
        "chat",
        {
            "type": "send_message",
            "message": message
        },
    )
