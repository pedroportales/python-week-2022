from typing import Optional
from sqlmodel import SQLModel, Field, select


class Beer(SQLModel, table=True):
    id: Optional[int] = Field(primary_key=True, default=None, index=True)
    name: str
    style: str
    flavor: float
    image: float
    cost: float
