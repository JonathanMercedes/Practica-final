from sqlmodel import Session, select
from models.user import User

def get_users(session: Session):
    return session.exec(select(User)).all()

def get_user_by_name(session: Session, name: str):
    statement = select(User).where(User.name == name)
    return session.exec(statement).first()