from pkg.mongodb.dbs import NotifyDB
from pkg.mongodb.views import NotificationDatabaseView


class NotificationRepository:
    _db = NotifyDB()

    async def record_to_send(self, notification: NotificationDatabaseView) -> NotificationDatabaseView | None:
        recorded_notification = await self._db.add_to_send(notification)
        return recorded_notification

    async def record_to_history(self, notification: NotificationDatabaseView) -> bool:
        response = await self._db.add_history(notification)
        return response
