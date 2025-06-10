from fastapi import APIRouter, Depends, HTTPException, Body
from sqlmodel import Session
from db.database import get_session
from models.order import Order
from models.orderProduct import OrderProduct
from crud.order import (
    get_orders,get_orders_by_user_name
)

router = APIRouter()


@router.get("/", response_model=list[Order])
def read_all(session: Session = Depends(get_session)):
    try:
        return get_orders(session)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Unexpected error: {str(e)}")
    
@router.get("/user/{user_name}", response_model=list[Order])
def read_by_user_name(user_name: str, session: Session = Depends(get_session)):
    try:
        orders = get_orders_by_user_name(session, user_name)
        if not orders:
            raise HTTPException(status_code=404, detail=f"No orders found for user '{user_name}'")
        return orders
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Unexpected error: {str(e)}")



