from pydantic import BaseModel as PydanticBaseModel, Extra, Field, constr

from exapi import utils
from exapi.bitget.v1.enums import Operation


class BaseModel(PydanticBaseModel):
    class Config:
        alias_generator = utils.to_lower_camel
        allow_population_by_field_name = True
        use_enum_values = True
        extra = Extra.forbid


class ResponseData(BaseModel):
    code: int
    msg: str
    data: list | dict | str | int | None = None
    request_time: int | None = None


class Topic(BaseModel):
    channel: constr(to_lower=True)  # Channel name
    inst_id: constr(to_upper=True)  # Instrument ID. Symbols in response field: symbol_name
    inst_type: constr(to_lower=True)  # Instrument type, SP: Spot public channel SPBL Spot private channel

    def __hash__(self) -> int:
        return hash(self.inst_type + self.channel + self.inst_id)


class Event(BaseModel):
    event: str  # Event, subscribe unsubscribe error
    topic: Topic | None = Field(None, alias='arg')  # Subscribed channel
    code: int = 0  # Error Code
    msg: str = ''  # Error Message


class Action(BaseModel):
    action: str  # Push data action, incremental or full data. update: incremental; snapshot: full
    topic: Topic = Field(..., alias='arg')  # Successfully subscribed channel
    data: list | dict  # Subscribed data


class Login(BaseModel):
    api_key: str
    passphrase: str
    timestamp: int
    sign: str


class Message(BaseModel):
    op: Operation
    args: list[Topic | Login]
