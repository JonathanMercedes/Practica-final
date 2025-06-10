from fastapi import FastAPI
from dotenv import load_dotenv
from routes import order,user,orderProduct
import uvicorn

# Load environment variables from .env file
load_dotenv()

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Welcome to the API"}

# Definir las rutas de la API
app.include_router(order.router, prefix="/api/orders", tags=["Orders"])

app.include_router(user.router, prefix="/api/users", tags=["Users"])

app.include_router(orderProduct.router, prefix="/api/orderProduct", tags=["OrderProduct"])


if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)


    