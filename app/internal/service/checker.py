from internal.objects.vendor import VendorModel, VendorHandler


class ApiKeyChecker:
    def __init__(self) -> None:
        self._vendor_handler = VendorHandler()

    async def get_expired_api_keys(self, vendor: VendorModel) -> VendorModel | None:
        expired_vendor = await self._check_vendor_api_key(vendor)
        return expired_vendor

    async def _check_vendor_api_key(self, vendor: VendorModel) -> VendorModel | None:
        api_key_correct = await self._vendor_handler.check_vendor_api_key(vendor)
        if api_key_correct is False:
            return vendor
        return None
