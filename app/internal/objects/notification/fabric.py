from datetime import datetime

from bson import ObjectId

from pkg.mongodb.views import NotificationDatabaseView
from .model import NotificationModel


class NotificationFabric:

    def create_model(self, chat_id: int, vendor_name: str) -> NotificationModel:
        return NotificationModel(
            created=datetime.now(),
            operation_date=datetime.now(),
            chat_id=chat_id,
            message=self._get_message(vendor_name),
            main=None,
            pin=True,
            status="prepared",
            is_system=True
        )

    @staticmethod
    def _get_message(vendor_name: str) -> str:
        message = (f"Обратите внимание, что для поставщика <b>{vendor_name}</b> у Вас используется "
                   "недействительный (срок действия ключа закончился) API ключ!\n\n"
                   "Вам необходимо выпустить новый ключ и отправить боту в сообщении.\n\n"
                   "📖<i>Инструкция:\n"
                   "  1️⃣ Зайдите в личный кабинет Wildberries"
                   " → Настройки → Доступ к API "
                   "<a href='https://seller.wildberries.ru/supplier-settings/access-to-api'>ссылка</a>).\n"
                   '  2️⃣ Нажмите "Создать новый токен".\n'
                   '  3️⃣ Введите имя "FenixWBBot", чтобы понимать для какого сервиса Вы выпустили ключ.'
                   ' Под каждый сервис ключ выпускайте отдельно во избежание задержек в получении данных.\n'
                   '  4️⃣ Выберите тип ключа "<b>Статистика</b>" и "<b>Контент</b>".\n'
                   "  5️⃣ Скопируйте токен и отправьте в сообщении боту,"
                   " дождитесь сообщения об обновлении ключа.</i>\n\n"
                   "<b>Ключ нужен один с доступом к 2ум разделам</b>\n\n"
                   "По всем возникающим вопросам обращайтесь в техподдержку @FenixWBSupport")
        return message

    @staticmethod
    def create_db_view(model: NotificationModel) -> NotificationDatabaseView:
        converted_main = ObjectId(model.main) if model.main is not None else None
        return NotificationDatabaseView(
            created=model.created,
            operation_date=model.operation_date,
            chat_id=model.chat_id,
            message=model.message,
            main=converted_main,
            pin=model.pin,
            status=model.status,
            is_system=model.is_system,
        )

    @staticmethod
    def create_model_by_db_view(db_view: NotificationDatabaseView) -> NotificationModel:
        converted_main = str(db_view.main) if db_view.main is not None else None
        return NotificationModel(
            created=db_view.created,
            operation_date=db_view.operation_date,
            chat_id=db_view.chat_id,
            message=db_view.message,
            main=converted_main,
            pin=db_view.pin,
            status=db_view.status,
            is_system=db_view.is_system
        )
