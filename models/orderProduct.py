from sqlmodel import SQLModel, Field

class OrderProduct(SQLModel, table=True):
    order: int = Field(foreign_key="order.id", primary_key=True)
    product: int = Field(primary_key=True)
    amount: int

class OrderProductDetailed(OrderProduct):
    productName: str
    description: str
    price: float
    