from .fabric import NotificationFabric
from .model import NotificationModel
from .repository import NotificationRepository


class NotificationHandler:
    _fabric = NotificationFabric()
    _repository = NotificationRepository()

    def create_notification(self, chat_id: int, vendor_name: str) -> NotificationModel:
        model = self._fabric.create_model(chat_id, vendor_name)
        return model

    async def record_notification(self, model: NotificationModel) -> NotificationModel | None:
        db_view = self._fabric.create_db_view(model)
        recorded_db_view = await self._repository.record_to_send(db_view)
        if recorded_db_view is None:
            return None
        recorded_model = self._fabric.create_model_by_db_view(recorded_db_view)
        return recorded_model

    async def record_history_notification(self, model: NotificationModel) -> bool:
        db_view = self._fabric.create_db_view(model)
        response = await self._repository.record_to_history(db_view)
        return response
