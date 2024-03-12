from bson import ObjectId
from motor_decorator import MotorDecoratorBaseDB, init_collection

from pkg.mongodb.views import VendorDatabaseView, UserDatabaseView


class VendorDB(MotorDecoratorBaseDB):
    CLUSTER = "MAIN"
    DATABASE = "F_VENDOR"
    VENDORS = "VENDORS"
    USERS = "USERS"

    @init_collection(VENDORS)
    async def get_vendors(self, vendor_ids: list[ObjectId]) -> list[VendorDatabaseView]:
        condition = {
            "_id": {"$in": vendor_ids},
            "KEY_NEW": {"$ne": None},
            "NEW_KEY_DISABLED": False,
            "SUPPLIER_ID": {
                "$ne": 0,
            }
        }
        projection = VendorDatabaseView.projection()
        vendors = await self.controller.do_find_many(condition, projection, VendorDatabaseView)
        return vendors

    @init_collection(USERS)
    async def get_users(self, vendor_ids: list[ObjectId]) -> list[UserDatabaseView]:
        condition: dict = {"VENDOR_ID": {"$in": vendor_ids}}
        projection = UserDatabaseView.projection()
        users = await self.controller.do_find_many(condition, projection, UserDatabaseView)
        return users

    @init_collection(VENDORS)
    async def disable_new_key(self, record_id: ObjectId) -> bool:
        condition: dict = {"_id": record_id}
        update = {"$set": {"NEW_KEY_DISABLED": True}}
        response = await self.controller.do_update_one(condition, update)
        return bool(response)
