import asyncio
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
        await self._run_processing(vendors)
        log.info(f"Finished validating vendors api keys: {time.time() - start:.2f} seconds")

    async def _get_vendors(self) -> list[VendorModel]:
        vendors = await self._vendor_handler.get_vendors()
        log.info(f"Received vendors {len(vendors)}")
        return vendors

    async def _run_processing(self, vendors: list[VendorModel]) -> None:
        amount = 0
        tasks = []
        for vendor in vendors:
            tasks.append(self._validate_vendor_api_key(vendor))

        for future in asyncio.as_completed(tasks):
            vendor_with_expired_key = await future
            if vendor_with_expired_key is None:
                continue
            amount += 1
            await self._create_notifications_for_vendor(vendor_with_expired_key)
            await self._disable_api_key(vendor_with_expired_key)
        log.info(f"Finished validating vendors api keys. Vendors with expired keys: {amount}")

    async def _validate_vendor_api_key(self, vendor: VendorModel) -> VendorModel | None:
        vendor_with_expired_key = await self._checker.get_expired_api_keys(vendor)

        if vendor_with_expired_key is None:
            log.debug(f"Vendor '{vendor.supplier_id}' has correct api key.")
        else:
            log.info(f"Vendor '{vendor.supplier_id}' has expired api key.")
        return vendor_with_expired_key

    async def _create_notifications_for_vendor(self, vendor: VendorModel) -> None:
        notification_amount = await self._notification_creator.handle_vendors_with_expired_api_key(vendor)
        log.info(f"Created notifications: {notification_amount}")

    async def _disable_api_key(self, vendor: VendorModel) -> None:
        response = await self._vendor_handler.disable_api_key(vendor)
        log.info(f"New api key disabled for '{vendor.name}({vendor.supplier_id}':"
                 f" {'successful' if response else 'unsuccessful'}")
