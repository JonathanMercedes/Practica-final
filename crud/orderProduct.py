from sqlmodel import Session, select
from models.orderProduct import OrderProduct
from models.user import User
from models.orderProduct import OrderProductDetailed
from crud.order import get_orders_by_user_name
from fastapi import Depends, HTTPException
import httpx


def get_detailed_orders(session: Session):
    return session.exec(select(OrderProduct)).all()

def get_detailed_order(session: Session, id: int):
    statement = select(OrderProduct).where(OrderProduct.order == id)
    return session.exec(statement).all()

async def get_detailed_orders_products(session: Session):

    detailedOrdersProducts = []

    try:
        detailedOrders = get_detailed_orders(session)

        for detailedOrder in detailedOrders:
            product = await fetch_product(detailedOrder.product)
            OrderProduct = OrderProductDetailed (
                order=detailedOrder.order,
                product=detailedOrder.product,
                productName = product["title"],
                description= product["description"],
                price=product["price"],
                amount= detailedOrder.amount
            )
            detailedOrdersProducts.append(OrderProduct)
    except Exception as e:
        raise Exception(e)
   
    if not detailedOrders:
        raise HTTPException(status_code=404, detail="Orders not found")
    return detailedOrdersProducts


async def get_detailed_order_products(session: Session, id: int):

    detailedOrdersProducts = []

    try:
        detailedOrders = get_detailed_order(session,id)

        for detailedOrder in detailedOrders:
            product = await fetch_product(detailedOrder.product)
            OrderProduct = OrderProductDetailed (
                order=detailedOrder.order,
                product=detailedOrder.product,
                productName = product["title"],
                description= product["description"],
                price=product["price"],
                amount= detailedOrder.amount
            )
            detailedOrdersProducts.append(OrderProduct)
    except Exception as e:
        raise Exception(e)
   
    if not detailedOrders:
        raise HTTPException(status_code=404, detail="Orders not found")
    return detailedOrdersProducts

async def get_detailed_order_products_by_user_name(session: Session, name: str):

    detailedOrdersProducts = []

    try:
        orders = get_orders_by_user_name(session,name)

        for order in orders:
            detailedOrders = get_detailed_order(session,order.id)

            for detailedOrder in detailedOrders:
                product = await fetch_product(detailedOrder.product)
                OrderProduct = OrderProductDetailed (
                    order=detailedOrder.order,
                    product=detailedOrder.product,
                    productName = product["title"],
                    description= product["description"],
                    price=product["price"],
                    amount= detailedOrder.amount
                )   
                detailedOrdersProducts.append(OrderProduct)
    except Exception as e:
        raise Exception(e)
   
    if not detailedOrders:
        raise HTTPException(status_code=404, detail="Orders not found")
    return detailedOrdersProducts


async def fetch_product(id:int):
    """Función para obtener los datos de la API externa."""
    url = "https://dummyjson.com/products/" + str(id)
    try:
        async with httpx.AsyncClient(verify=False) as client:
            response = await client.get(url, timeout=10.0)
            response.raise_for_status()
            data = response.json()
            product = {
                    "title": data["title"],
                    "description": data["description"],
                    "category": data["category"],
                    "price": data["price"],
                    "discountPercentage": data["discountPercentage"],
                    "rating": data["rating"],
                    "stock": data["stock"]
            }
                         
            return product
    except httpx.RequestError as e:
        raise Exception(f"Error de conexión al consultar la API externa: {str(e)}")
    except httpx.HTTPStatusError as e:
        raise Exception(f"Respuesta inválida de la API externa: {e.response.status_code}")
    except Exception as e:
        raise Exception(f"Ocurrió un error inesperado: {str(e)}")