from sqlalchemy.orm import Session
from app.models.expense import Expense

def crear_gasto(db: Session, chat_id: int, category: str, amount: float):
    gasto = Expense(chat_id=chat_id, category=category, amount=amount)
    db.add(gasto)
    db.commit()
    db.refresh(gasto)
    return gasto

def obtener_gastos(db: Session, chat_id: int):
    return db.query(Expense).filter(Expense.chat_id == chat_id).all()