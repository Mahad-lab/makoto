from enum import Enum as PythonEnum

from sqlalchemy import Column, Enum, String

from app.core.database import Base
from app.utils.constant.globals import UserRole

from .common import CommonModel


class User(CommonModel):
    __tablename__ = "users"

    first_name = Column(String(50), nullable=True)
    last_name = Column(String(50), nullable=True)
    email = Column(String(50), unique=True, index=True)
    password = Column(
        String(100), nullable=True
    )  # nullable=True for social auth(OAuth2)
    role = Column(Enum(UserRole), default=UserRole.USER)

    def __repr__(self):
        return f"{self.email}"


metadata = Base.metadata
