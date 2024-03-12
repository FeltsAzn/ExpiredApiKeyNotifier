from internal.objects.core_model import CoreModel


class VendorModel(CoreModel):
    id: str
    name: str
    supplier_id: int
    api_key: str
    members: list[int]
