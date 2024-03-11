from internal.objects.notification import NotificationHandler, NotificationModel
from internal.objects.vendor import VendorModel
from utils import log


class NotificationCreator:
    def __init__(self) -> None:
        self._notification_handler = NotificationHandler()

    async def handle_vendors_with_expired_api_key(self, vendors: list[VendorModel]) -> int:
        notifications = await self._create_notifications(vendors)
        notifications_amount = await self._record_notifications(notifications)
        return notifications_amount

    async def _create_notifications(self, vendors: list[VendorModel]) -> list[NotificationModel]:
        notifications = []

        for vendor in vendors:
            for member in vendor.members:
                notification = self._notification_handler.create_notification(member)
                notifications.append(notification)
        return notifications

    async def _record_notifications(self, notifications: list[NotificationModel]) -> int:
        notifications_amount = 0
        for notification in notifications:
            recorded_notification = await self._notification_handler.record_notification(notification)
            if recorded_notification:
                response = await self._notification_handler.record_history_notification(recorded_notification)
                log.info(f"Created notification to change api key for '{notification.chat_id}' user:"
                         f" {'successfully' if response else 'unsuccessfully'}")
                notifications_amount += 1
            else:
                log.warning(f"Not recorded notification to change api key for '{notification.chat_id}' user")

        return notifications_amount
