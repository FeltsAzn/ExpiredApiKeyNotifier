import asyncio

from pkg.mongodb.dbs import VendorDB, UserDB
from pkg.mongodb.views import VendorDatabaseView, UserDatabaseView
from pkg.network import WildBerriesController
from utils import log
from .model import VendorModel


class VendorRepository:
    _vendor_db = VendorDB()
    _user_db = UserDB()
    _network = WildBerriesController()
    _semaphore = asyncio.Semaphore(100)

    async def get_vendors(self) -> list[VendorDatabaseView]:
        vendors = await self._vendor_db.get_vendors()
        log.debug(f"Received raw vendors from Vendor database: {len(vendors)}")
        return vendors

    async def get_users(self) -> list[UserDatabaseView]:
        users = await self._vendor_db.get_users()
        log.debug(f"Received raw users from Vendor database: {len(users)}")
        return users

    async def user_is_blocked(self, user: UserDatabaseView) -> UserDatabaseView:
        async with self._semaphore:
            specified_user = await self._user_db.user_is_blocked(user)
        return specified_user

    async def validate_api_key(self, vendor: VendorModel) -> bool | None:
        api_key = vendor.api_key
        response = await self._network.validate_api_key(api_key)
        return response
