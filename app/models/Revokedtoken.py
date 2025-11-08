from sqlalchemy import Column, DateTime, Integer, String, Text 
from dB.base import Base

class RevokedToken(Base):
    __tablename__ = "revoked_tokens"
    id = Column(Integer, primary_key=True, index=True)
    jti = Column(String(64), unique=True, index=True, nullable=False)
    expires_at = Column(DateTime, nullable=False)
    reason = Column(Text, nullable=True)
