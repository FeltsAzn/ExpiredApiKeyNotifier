from bson import ObjectId
from motor_decorator import MotorDecoratorBaseDB, init_collection


class SubscriptionDB(MotorDecoratorBaseDB):
    CLUSTER = "MAIN"
    DATABASE = "F_SUBSCRIPTION"
    SUBSCRIPTIONS = "SUBSCRIPTIONS"

    @init_collection(SUBSCRIPTIONS)
    async def find_active_subscriptions(self) -> list[ObjectId]:
        pipeline = [
            {
                "$match": {
                    "ACTIVE": True,
                },
            },
            {
                "$group": {
                    "_id": "$VENDOR_ID",
                },
            },
            {
                "$project": {
                    "_id": 0,
                    "VENDOR_ID": "$_id",
                },
            },
        ]

        raw_records: list = await self.controller.do_aggregate(pipeline)
        subscriptions = [raw_record["VENDOR_ID"] for raw_record in raw_records]
        return subscriptions
