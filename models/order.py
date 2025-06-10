from sqlmodel import SQLModel, Field

class Order(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    user: int = Field(foreign_key="user.id")

