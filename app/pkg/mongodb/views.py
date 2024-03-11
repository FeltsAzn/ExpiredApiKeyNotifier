from datetime import datetime
from typing import Self

from bson import ObjectId
from motor_decorator import MotorDecoratorAbstractView
from pydantic import Field


class VendorDatabaseView(MotorDecoratorAbstractView):
    id: ObjectId
    NAME: str
    SUPPLIER_ID: int
    KEY_NEW: str
    MEMBERS: list[int] = Field(default_factory=list)

    @classmethod
    def from_db(cls, data: dict) -> Self:
        data["id"] = data.pop("_id")
        return cls(**data)


class UserDatabaseView(MotorDecoratorAbstractView):
    VENDOR_ID: ObjectId
    USER_ID: int
    BLOCKED: bool = False

    @classmethod
    def from_db(cls, data: dict) -> Self:
        return cls(**data)


class NotificationDatabaseView(MotorDecoratorAbstractView):
    created: datetime
    operation_date: datetime
    chat_id: int
    message: str
    main: ObjectId | None = None
    pin: bool
    status: str
    media_type: str
    media: str
    keyboard: str

    @classmethod
    def from_db(cls, data: dict) -> Self:
        return cls(**data)

    def set_main_id(self, record_id: ObjectId) -> None:
        self.main = record_id

    def to_send(self) -> dict:
        return {
            "CREATED": self.created,
            "CHAT": self.chat_id,
            "MESSAGE": self.message,
            "pin": self.pin,
            "media_type": self.media_type,
            "media": self.media,
            "keyboard": self.keyboard,
            "STATUS": self.status
        }

    def to_history(self) -> dict:
        assert self.message is not None
        return {
            "CREATED": self.created,
            "CHAT": self.chat_id,
            "MESSAGE": self.message,
            "MAIN": self.main,
            "pin": self.pin,
            "media_type": self.media_type,
            "media": self.media,
            "keyboard": self.keyboard,
            "STATUS": self.status
        }
