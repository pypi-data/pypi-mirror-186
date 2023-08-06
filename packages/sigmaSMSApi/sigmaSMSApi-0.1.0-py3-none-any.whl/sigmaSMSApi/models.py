import enum
from re import fullmatch

from pydantic import BaseModel


class RusMobilePhone(str):
    @classmethod
    def __get_validators__(cls):
        yield cls.validate

    @classmethod
    def validate(cls, value):
        if not isinstance(value, str):
            raise TypeError('must be string')

        if not fullmatch(r'(\+)[7][0-9\-\(\)\.]{10}$', value):
            raise ValueError('format must be +7xxxxxxxxxx')

        return value


class TypeMessage(enum.Enum):
    SMS = 'sms'
    MMS = 'mms'
    VIBER = 'viber'
    WHATSAPP = 'whatsapp'
    VK = 'vk'
    VOICE = 'voice'
    FLASHCALL = 'flashcall'
    OK = 'ok'


class Payload(BaseModel):
    sender: str = 'DELFIN'
    text: str


class BaseMessage(BaseModel):
    recipient: RusMobilePhone
    type: TypeMessage
    payload: Payload


class SMSMessage(BaseMessage):
    type = TypeMessage.SMS


class StatusMessage(enum.Enum):
    PENDING = 'pending'
    PAUSED = 'paused'
    PROCESSING = 'processing'
    SENT = 'sent'
    DELIVERED = 'delivered'
    SEEN = 'seen'
    FAILED = 'failed'


class SentMessage(BaseModel):
    id: str
    recipient: str
    status: StatusMessage
    error: str = None
