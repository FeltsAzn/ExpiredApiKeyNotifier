from pkg.mongodb.views import VendorDatabaseView
from .model import VendorModel


class VendorFabric:
    @staticmethod
    def create_model_from_db_view(db_view: VendorDatabaseView) -> VendorModel:
        return VendorModel(
            supplier_id=db_view.SUPPLIER_ID,
            api_key=db_view.KEY_NEW,
            members=db_view.MEMBERS
        )
