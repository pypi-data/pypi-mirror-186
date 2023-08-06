from pydantic import BaseModel as PydanticBaseModel, Extra

from exapi import utils
from exapi.bybit.v3.enums import Operation


class BaseModel(PydanticBaseModel):
    class Config:
        alias_generator = utils.to_lower_camel
        allow_population_by_field_name = True
        use_enum_values = True
        extra = Extra.forbid


class ResponseData(BaseModel):
    ret_code: int
    ret_msg: str
    result: dict
    ret_ext_map: dict | None = None
    ret_ext_info: dict | None = None
    time: int


class Message(BaseModel):
    op: Operation
    args: list[str]
    req_id: str | None = None
