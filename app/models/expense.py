from sqlalchemy import Column, Integer, String, Float, DateTime, BigInteger
from app.db.database import Base
from pydantic import BaseModel
from datetime import datetime, timezone

class Expense(Base):
    __tablename__ = "expenses"

    id = Column(Integer, primary_key=True, index=True)
    chat_id = Column(BigInteger, nullable=False)  # ID del usuario en Telegram
    category = Column(String, nullable=False)
    amount = Column(Float, nullable=False)
    created_at = Column(DateTime, default=datetime.now(timezone.utc))