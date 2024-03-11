import asyncio

from pkg.mongodb.views import UserDatabaseView, VendorDatabaseView
from .fabric import VendorFabric
from .model import VendorModel
from .repository import VendorRepository


class VendorHandler:
    _fabric = VendorFabric()
    _repository = VendorRepository()

    async def get_vendors(self) -> list[VendorModel]:
        vendor_db_views = await self._repository.get_vendors()
        user_db_views = await self._repository.get_users()
        filtered_user_db_views = await self._filter_users(user_db_views)
        specified_vendor_db_views = self._set_members_to_vendors(vendor_db_views, filtered_user_db_views)
        models = [self._fabric.create_model_from_db_view(db_view) for db_view in specified_vendor_db_views]
        return models

    async def _filter_users(self, users_db_views: list[UserDatabaseView]) -> list[UserDatabaseView]:
        tasks = [self._repository.user_is_blocked(user) for user in users_db_views]
        results = await asyncio.gather(*tasks)
        return [user for user in results if user.BLOCKED is False]

    @staticmethod
    def _set_members_to_vendors(
            vendors_db_views: list[VendorDatabaseView],
            users_db_views: list[UserDatabaseView]
    ) -> list[VendorDatabaseView]:

        for vendor in vendors_db_views:
            members = []
            for user in users_db_views:
                if user.VENDOR_ID == vendor.id:
                    members.append(user.USER_ID)
            vendor.MEMBERS = members
        return vendors_db_views

    async def check_vendor_api_key(self, model: VendorModel) -> bool | None:
        response = await self._repository.validate_api_key(model)
        return response
