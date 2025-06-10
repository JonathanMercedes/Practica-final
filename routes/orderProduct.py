from fastapi import APIRouter, Depends, HTTPException, Body
from sqlmodel import Session
from db.database import get_session
from models.orderProduct import OrderProduct,OrderProductDetailed
from crud.orderProduct import (
    get_detailed_order_products,get_detailed_orders_products,get_detailed_order_products_by_user_name
)

router = APIRouter()


@router.get("/", response_model=list[OrderProductDetailed])
async def read_detailed(session: Session = Depends(get_session)):
    return await get_detailed_orders_products(session)


@router.get("/id/{id}", response_model=list[OrderProductDetailed])
async def read_detailed_by_id(id: int,session: Session = Depends(get_session)):
    try:
        orderProducts = await get_detailed_order_products(session, id)
        if not orderProducts:
            raise HTTPException(status_code=404, detail=f"order with id '{id}' not found")
        return orderProducts
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Unexpected error: {str(e)}")
    
@router.get("/username/{username}", response_model=list[OrderProductDetailed])
async def read_detailed_by_user_name(name: str,session: Session = Depends(get_session)):
    try:
        orderProducts = await get_detailed_order_products_by_user_name(session, name)
        if not orderProducts:
            raise HTTPException(status_code=404, detail=f"order with name '{name}' not found")
        return orderProducts
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Unexpected error: {str(e)}")
    

    