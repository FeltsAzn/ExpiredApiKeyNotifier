from datetime import datetime

from bson import ObjectId

from pkg.mongodb.views import NotificationDatabaseView
from .model import NotificationModel


class NotificationFabric:

    @staticmethod
    def create_model(chat_id: int) -> NotificationModel:
        return NotificationModel(
            created=datetime.now(),
            operation_date=datetime.now(),
            chat_id=chat_id,
            message="SOME MESSAGE",
            main=None,
            pin=True,
            status="prepared",
            media_type="",
            media="",
            keyboard="",
        )

    @staticmethod
    def create_db_view(model: NotificationModel) -> NotificationDatabaseView:
        converted_main = ObjectId(model.main) if model.main is not None else None
        return NotificationDatabaseView(
            created=model.created,
            operation_date=model.operation_date,
            chat_id=model.chat_id,
            message=model.message,
            main=converted_main,
            pin=model.pin,
            status=model.status,
            media_type=model.media_type,
            media=model.media,
            keyboard=model.keyboard
        )

    @staticmethod
    def create_model_by_db_view(db_view: NotificationDatabaseView) -> NotificationModel:
        converted_main = str(db_view.main) if db_view.main is not None else None
        return NotificationModel(
            created=db_view.created,
            operation_date=db_view.operation_date,
            chat_id=db_view.chat_id,
            message=db_view.message,
            main=converted_main,
            pin=db_view.pin,
            status=db_view.status,
            media_type=db_view.media_type,
            media=db_view.media,
            keyboard=db_view.keyboard
        )
