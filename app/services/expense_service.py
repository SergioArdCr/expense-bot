from sqlalchemy.orm import Session
from app.models.expense import Expense
from datetime import datetime, timezone

def crear_gasto(db: Session, chat_id: int, category: str, amount: float):
    gasto = Expense(chat_id=chat_id, category=category, amount=amount)
    db.add(gasto)
    db.commit()
    db.refresh(gasto)
    return gasto

def obtener_gastos(db: Session, chat_id: int):
    return db.query(Expense).filter(Expense.chat_id == chat_id).all()

def borrar_gastos_mes(db: Session, chat_id: int):
    ahora = datetime.now(timezone.utc)
    inicio_mes = ahora.replace(day=1, hour=0, minute=0, second=0, microsecond=0)
    
    eliminados = (
        db.query(Expense)
        .filter(Expense.chat_id == chat_id, Expense.created_at >= inicio_mes)
        .delete()
    )
    db.commit()
    return eliminados