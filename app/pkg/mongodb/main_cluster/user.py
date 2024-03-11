from motor_decorator import MotorDecoratorBaseDB, init_collection

from pkg.mongodb.views import UserDatabaseView


class UserDB(MotorDecoratorBaseDB):
    CLUSTER = "MAIN"
    DATABASE = "F_USER"
    USERS = "USERS"

    @init_collection(USERS)
    async def user_is_blocked(self, user: UserDatabaseView) -> UserDatabaseView:
        condition = {
            "ID": user.USER_ID,
            "BLOCKED": True
        }
        projection = {"_id": 1}
        record = await self.controller.do_find_one(condition, projection)
        if isinstance(record, dict):
            user.BLOCKED = True
        return user
