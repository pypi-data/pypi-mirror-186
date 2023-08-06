from pydantic import constr

from exapi.bitget.v1.models import BaseModel


class ProductParams(BaseModel):
    symbol: constr(to_upper=True)
