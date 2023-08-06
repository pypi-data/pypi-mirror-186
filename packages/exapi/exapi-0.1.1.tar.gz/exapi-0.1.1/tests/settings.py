from pydantic import BaseSettings


class Settings(BaseSettings):
    BYBIT_API_KEY: str = 'KEY'
    BYBIT_API_SECRET: str = 'SECRET'

    BITGET_API_KEY: str = 'KEY'
    BITGET_API_SECRET: str = 'SECRET'
    BITGET_API_PASSPHRASE: str = 'PASSPHRASE'

    class Config:
        case_sensitive = True
