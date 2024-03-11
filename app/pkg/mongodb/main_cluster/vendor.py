from motor_decorator import MotorDecoratorBaseDB, init_collection

from pkg.mongodb.views import VendorDatabaseView, UserDatabaseView


class VendorDB(MotorDecoratorBaseDB):
    CLUSTER = "MAIN"
    DATABASE = "F_VENDOR"
    VENDORS = "VENDORS"
    USERS = "USERS"

    @init_collection(VENDORS)
    async def get_vendors(self) -> list[VendorDatabaseView]:
        condition = {
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
    async def get_users(self) -> list[UserDatabaseView]:
        condition = {}
        projection = UserDatabaseView.projection()
        users = await self.controller.do_find_many(condition, projection, UserDatabaseView)
        return users
