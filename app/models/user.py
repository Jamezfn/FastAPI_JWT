from sqlalchemy import Column, Integer, String, Boolean
from dB.base import Base

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    username = Column(String(128), unique=True, index=True, nullable=False)
    hash_password = Column(String(256), nullable=False)
    is_active = Column(Boolean, default=True)
