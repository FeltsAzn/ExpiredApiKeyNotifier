import asyncio

from internal.objects.vendor import VendorModel, VendorHandler


class ApiKeyChecker:
    def __init__(self) -> None:
        self._vendor_handler = VendorHandler()

    async def get_expired_api_keys(self, vendors: list[VendorModel]) -> list[VendorModel]:
        tasks = [self._check_vendor_api_key(vendor) for vendor in vendors]
        checked_vendors = await asyncio.gather(*tasks)
        vendors_with_expired_api_keys = [vendor for vendor in checked_vendors if vendor]
        return vendors_with_expired_api_keys

    async def _check_vendor_api_key(self, vendor: VendorModel) -> VendorModel | None:
        api_key_correct = await self._vendor_handler.check_vendor_api_key(vendor)
        if api_key_correct is True:
            return None
        return vendor
