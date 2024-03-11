from internal.objects.core_model import CoreModel


class VendorModel(CoreModel):
    supplier_id: int
    api_key: str
    members: list[int]
