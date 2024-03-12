import asyncio

from bson import ObjectId

from pkg.mongodb.dbs import VendorDB, UserDB, SubscriptionDB
from pkg.mongodb.views import VendorDatabaseView, UserDatabaseView
from pkg.network import WildBerriesController
from utils import log
from .model import VendorModel


class VendorRepository:
    _subscription_db = SubscriptionDB()
    _vendor_db = VendorDB()
    _user_db = UserDB()
    _network = WildBerriesController()

    def __init__(self) -> None:
        self._semaphore = asyncio.Semaphore(100)

    async def get_premium_vendor_ids(self) -> list[ObjectId]:
        vendors = await self._subscription_db.find_active_subscriptions()
        log.debug(f"Received active subs from Subscription database: {len(vendors)}")
        return vendors

    async def get_vendors(self, vendor_ids: list[ObjectId]) -> list[VendorDatabaseView]:
        vendors = await self._vendor_db.get_vendors(vendor_ids)
        log.debug(f"Received raw vendors from Vendor database: {len(vendors)}")
        return vendors

    async def get_users(self, vendor_ids: list[ObjectId]) -> list[UserDatabaseView]:
        users = await self._vendor_db.get_users(vendor_ids)
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

    async def disable_api_key(self, vendor: VendorModel) -> bool:
        record_id = ObjectId(vendor.id)
        response = await self._vendor_db.disable_new_key(record_id)
        return response
