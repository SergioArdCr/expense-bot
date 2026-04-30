from fastapi import FastAPI
from contextlib import asynccontextmanager
from telegram.ext import ApplicationBuilder, MessageHandler, filters
from app.bot.handlers import handle_message
import os
from dotenv import load_dotenv

load_dotenv()

TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")

@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup
    application = ApplicationBuilder().token(TELEGRAM_TOKEN).build()
    application.add_handler(MessageHandler(filters.TEXT, handle_message))
    await application.initialize()
    await application.start()
    await application.updater.start_polling()
    
    yield  # ← app corre aquí
    
    # Shutdown
    await application.updater.stop()
    await application.stop()
    await application.shutdown()

app = FastAPI(lifespan=lifespan)

@app.get("/health")
def health():
    return {"status": "ok"}