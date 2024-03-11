from internal.objects.core_model import CoreModel


class VendorModel(CoreModel):
    name: str
    supplier_id: int
    api_key: str
    members: list[int]
