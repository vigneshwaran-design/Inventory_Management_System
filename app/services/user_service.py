from sqlalchemy.orm import Session
from fastapi import HTTPException
from passlib.context import CryptContext
from ..models.user_model import User
from ..schema.user_schema import UserCreate
from ..auth import hash_password, verify_password


class UserService:

    @staticmethod
    def register(db: Session, data: UserCreate):
        # check if username exists
        existing_user = db.query(User).filter(User.username == data.username).first()
        if existing_user:
            raise HTTPException(status_code=400, detail="Username already exists")

        # hash password
        hashed_pw = hash_password(data.password)

        # create user
        user = User(
            username=data.username,
            email=data.email,
            hashed_password=hashed_pw
        )
        db.add(user)
        db.commit()
        db.refresh(user)
        return user

    @staticmethod
    def authenticate(db: Session, username: str, password: str):
        user = db.query(User).filter(User.username == username).first()

        if not user:
            return None

        # verify password with hashed password
        if not verify_password(password, user.hashed_password):
            return None

        return user

    @staticmethod
    def get_user_by_username(db: Session, username: str):
        return db.query(User).filter(User.username == username).first()
