from pydantic import BaseModel, ConfigDict


class CoreModel(BaseModel):
    model_config = ConfigDict(arbitrary_types_allowed=True, extra="forbid")
