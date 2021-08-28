from typing import Optional

from pydantic import HttpUrl
from sqlmodel import Field, SQLModel


class RedirectBase(SQLModel):
    name: str
    url: HttpUrl


class Redirect(RedirectBase, table=True):
    id: Optional[int] = Field(None, primary_key=True)


class RedirectCreate(RedirectBase):
    ...
