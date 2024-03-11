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
    is_system: bool
    status: str

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
            "STATUS": self.status,
            "SYSTEM": self.is_system
        }

    def to_history(self) -> dict:
        assert self.main is not None
        return {
            "CREATED": self.created,
            "CHAT": self.chat_id,
            "MESSAGE": self.message,
            "MAIN": self.main,
            "pin": self.pin,
            "STATUS": self.status,
            "SYSTEM": self.is_system
        }
