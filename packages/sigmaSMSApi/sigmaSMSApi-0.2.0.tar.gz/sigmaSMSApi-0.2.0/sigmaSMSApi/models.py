import enum
from typing import NamedTuple, Union


class Response(NamedTuple):
    status: int
    content: Union[str, dict] = None


class TypeMessage(enum.Enum):
    SMS = 'sms'
    MMS = 'mms'
    VIBER = 'viber'
    WHATSAPP = 'whatsapp'
    VK = 'vk'
    VOICE = 'voice'
    FLASHCALL = 'flashcall'
    OK = 'ok'


class StatusMessage(enum.Enum):
    PENDING = 'pending'
    PAUSED = 'paused'
    PROCESSING = 'processing'
    SENT = 'sent'
    DELIVERED = 'delivered'
    SEEN = 'seen'
    FAILED = 'failed'
