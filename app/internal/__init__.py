import time

from internal.objects.vendor import VendorHandler, VendorModel
from internal.service.checker import ApiKeyChecker
from internal.service.notification_creator import NotificationCreator
from utils import log


class ExpiredApiKeyNotifierApplication:

    def __init__(self) -> None:
        self._checker = ApiKeyChecker()
        self._vendor_handler = VendorHandler()
        self._notification_creator = NotificationCreator()

    async def run(self) -> None:
        start = time.time()
        log.info(f"Starting validating vendors api keys")
        vendors = await self._get_vendors()
        vendors_with_expired_api_key = await self._get_vendors_with_expired_api_key(vendors)
        await self._create_notifications(vendors_with_expired_api_key)
        log.info(f"Finished validating vendors api keys: {time.time() - start:.2f} seconds")

    async def _get_vendors(self) -> list[VendorModel]:
        vendors = await self._vendor_handler.get_vendors()
        log.info(f"Received vendors {len(vendors)}")
        return vendors

    async def _get_vendors_with_expired_api_key(self, vendors: list[VendorModel]) -> list[VendorModel]:
        vendors_with_expired_api_key = await self._checker.get_expired_api_keys(vendors)
        log.info(f"Vendors with expired api keys: {len(vendors_with_expired_api_key)}")
        return vendors_with_expired_api_key

    async def _create_notifications(self, vendors: list[VendorModel]) -> None:
        notification_amount = await self._notification_creator.handle_vendors_with_expired_api_key(vendors)
        log.info(f"Created notifications: {notification_amount}")
