from datetime import datetime

from internal.objects.core_model import CoreModel


class NotificationModel(CoreModel):
    created: datetime
    operation_date: datetime
    chat_id: int
    message: str
    main: str | None
    pin: bool
    status: str
    is_system: bool
