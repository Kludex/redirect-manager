from typing import Any, Optional

from pydantic import BaseSettings, SecretStr, validator


class Settings(BaseSettings):
    POSTGRES_DB: str
    POSTGRES_HOST: str
    POSTGRES_USER: str
    POSTGRES_PASSWORD: SecretStr
    # TODO(Marcelo): Change type once https://github.com/samuelcolvin/pydantic/pull/2567 is merged.
    POSTGRES_URI: Optional[str] = None

    @validator("POSTGRES_URI", pre=True)
    def validate_postgres_conn(cls, v: Optional[str], values: dict[str, Any]) -> str:
        if isinstance(v, str):
            return v
        password: SecretStr = values.get("POSTGRES_PASSWORD", SecretStr(""))
        return "{scheme}://{user}:{password}@{host}/{db}".format(
            scheme="postgresql+asyncpg",
            user=values.get("POSTGRES_USER"),
            password=password.get_secret_value(),
            host=values.get("POSTGRES_HOST"),
            db=values.get("POSTGRES_DB"),
        )


settings = Settings()
