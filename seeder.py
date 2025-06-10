from sqlmodel import SQLModel, Session
from db.database import engine, create_db_and_tables, drop_db_and_tables
from models.user import User
from models.order import Order
from models.orderProduct import OrderProduct
from auth.hashing import hash_password  # Importamos la función para hashear contraseñas

def seed_data():
    # Borrar la base de datos y las tablas existentes
    drop_db_and_tables() 
    # Crear la base de datos y las tablas
    create_db_and_tables()

    with Session(engine) as session:
        # Crear usuarios
        try:
            user1 = User(name="user1", email="user1@example.com", hashed_password=hash_password("password1"), role="user")
            user2 = User(name="user2", email="user2@example.com", hashed_password=hash_password("password2"), role="user")
            admin1 = User(name="admin1", email="admin1@example.com", hashed_password=hash_password("adminpassword1"), role="admin")
            admin2 = User(name="admin2", email="admin2@example.com", hashed_password=hash_password("adminpassword2"), role="admin")
            session.add_all([user1, user2, admin1, admin2])
            session.commit()
        except Exception as e:
            print(f"Error creating users: {e}")

        # Crear pedidos
        try:
            order1 = Order(user=1)
            order2 = Order(user=2)
            
            session.add_all([order1, order2])
            session.commit()
        except Exception as e:
            print(f"Error creating orders: {e}")

        # Crear pedidosUsuarios
        try:
            orderProduct1 = OrderProduct(order=1,product=1,amount=1)
            orderProduct2 = OrderProduct(order=1,product=2,amount=2)
            orderProduct3 = OrderProduct(order=2,product=3,amount=2)
            orderProduct4 = OrderProduct(order=2,product=4,amount=4)
            session.add_all([orderProduct1, orderProduct2,orderProduct3,orderProduct4])
            session.commit()
        except Exception as e:
            print(f"Error creating orders: {e}")


       

if __name__ == "__main__":
    seed_data()
