from pydantic import BaseModel
from datetime import datetime

class ExpenseCreate(BaseModel):
    chat_id: int
    category: str
    amount: float

class ExpenseOut(BaseModel):
    id: int
    category: str
    amount: float
    created_at: datetime

    class Config:
        from_attributes = True