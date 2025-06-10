from fastapi import APIRouter, Depends, HTTPException, Body
from sqlmodel import Session
from db.database import get_session
from models.user import User
from crud.user import (
    get_users,get_user_by_name
)

router = APIRouter()


@router.get("/", response_model=list[User])
def read_all(session: Session = Depends(get_session)):
    try:
        return get_users(session)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Unexpected error: {str(e)}")
    

@router.get("/name/{name}", response_model=User)
def read_by_name(name: str,session: Session = Depends(get_session)):
    try:
        user = get_user_by_name(session, name)
        if not user:
            raise HTTPException(status_code=404, detail=f"User with name '{name}' not found")
        return user
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Unexpected error: {str(e)}")
    

