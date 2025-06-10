from sqlmodel import Session, select
from models.order import Order
from models.user import User
from models.orderProduct import OrderProductDetailed
from fastapi import Depends, HTTPException
from crud.user import get_user_by_name
import httpx

def get_orders(session: Session):
    return session.exec(select(Order)).all()

def get_orders_by_user_name(session: Session, user_name: str):
    user = get_user_by_name(session, user_name)
    if not user:
        return []
    statement = select(Order).where(Order.user == user.id)
    return session.exec(statement).all()





