from telegram import Update
from telegram.ext import ContextTypes
from app.bot.parser import parsear_gasto
from app.services.expense_service import crear_gasto, obtener_gastos, borrar_gastos_mes
from app.db.database import SessionLocal

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    texto = update.message.text
    chat_id = update.message.chat_id
    db = SessionLocal()

    try:
        # Comando para ver resumen
        if texto.lower() in ["gastos", "resumen", "/gastos"]:
            gastos = obtener_gastos(db, chat_id)
            if not gastos:
                await update.message.reply_text("No tienes gastos registrados.")
                return

            total = sum(g.amount for g in gastos)
            lineas = [f"• {g.category}: ${g.amount:,.0f}" for g in gastos]
            resumen = "\n".join(lineas) + f"\n\nTotal: ${total:,.0f}"
            await update.message.reply_text(resumen)
            return
        
        # Comando para borrar gastos del mes
        if texto.lower() in ["/borrar", "borrar"]:
            eliminados = borrar_gastos_mes(db, chat_id)
            await update.message.reply_text(
                f"🗑️ {eliminados} gasto(s) del mes eliminados."
            )
            return

        # Intentar parsear como gasto
        categoria, monto = parsear_gasto(texto)
        if categoria is None:
            await update.message.reply_text(
                "No entendí. Escribe así:\nAlmuerzo 15000"
            )
            return

        crear_gasto(db, chat_id, categoria, monto)
        await update.message.reply_text(
            f"✅ Gasto registrado\n{categoria}: ${monto:,.0f}"
        )

    finally:
        db.close()