from bson import ObjectId
from motor_decorator import MotorDecoratorBaseDB, init_collection

from pkg.mongodb.views import NotificationDatabaseView


class NotifyDB(MotorDecoratorBaseDB):
    CLUSTER = "MAIN"
    DATABASE = "F_NOTIFY"
    NOTIFICATIONS = "NOTIFICATIONS"
    HISTORY_NOTIFICATIONS = "HISTORY_NOTIFICATIONS"

    @init_collection(NOTIFICATIONS)
    async def add_to_send(self, notification: NotificationDatabaseView) -> NotificationDatabaseView | None:
        record = notification.to_send()
        record_id = await self.controller.do_insert_one(record, return_id=True)
        if isinstance(record_id, ObjectId):
            notification.set_main_id(record_id)
            return notification
        return None

    @init_collection(HISTORY_NOTIFICATIONS)
    async def add_history(self, notification: NotificationDatabaseView) -> bool:
        record = notification.to_history()
        response = await self.controller.do_insert_one(record)
        return response
