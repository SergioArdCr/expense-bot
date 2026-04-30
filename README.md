# 🤖 Expense Bot (Español)

---

## 📌 Descripción

Bot de Telegram para registrar y consultar gastos personales en lenguaje natural.
Escribe `Almuerzo 15000` y el bot guarda el gasto en PostgreSQL, muestra resúmenes y permite limpiar el mes.
Cambia automáticamente entre polling (local) y webhook (producción en Railway).

Proyecto desarrollado como parte de un plan de aprendizaje de Python enfocado en desarrollo backend.

**GitHub:** https://github.com/SergioArdCr/expense-bot  
**Railway:** https://expense-bot-production-de35.up.railway.app

---

## 🛠️ Tecnologías

| Librería | Uso |
|---|---|
| `FastAPI` | Framework web para recibir el webhook de Telegram |
| `python-telegram-bot` | Interacción con la API de Telegram |
| `SQLAlchemy` | ORM para manejo de base de datos |
| `PostgreSQL` | Almacenamiento de gastos |
| `Alembic` | Migraciones de base de datos |
| `Docker Compose` | Orquestación de contenedores (api + db) |

---

## 📁 Estructura

```
expense-bot/
├── app/
│   ├── bot/
│   │   ├── handlers.py         # Manejo de mensajes de Telegram
│   │   └── parser.py           # Parsing de texto a datos estructurados
│   ├── db/
│   │   └── session.py          # Conexión PostgreSQL
│   ├── models/
│   │   └── expense.py          # Modelo de gastos
│   ├── schemas/
│   │   └── expense.py          # Validación con Pydantic
│   ├── services/
│   │   └── expense_service.py  # Lógica CRUD
│   └── main.py                 # FastAPI + webhook/polling automático
├── alembic/                    # Migraciones
├── docker-compose.yml
├── Dockerfile
├── .env.example
└── requirements.txt
```

---

## ⚙️ Instalación

```bash
# Clonar el repositorio
git clone https://github.com/SergioArdCr/expense-bot.git
cd expense-bot

# Crear entorno virtual
python -m venv venv
venv\Scripts\activate       # Windows
source venv/bin/activate    # Mac/Linux

# Instalar dependencias
pip install -r requirements.txt

# Configurar variables de entorno
cp .env.example .env
# Editar .env con tus valores

# Levantar contenedores
docker-compose up --build

# Correr migraciones
docker-compose exec api alembic upgrade head
```

---

## 🔐 Variables de entorno

```env
DATABASE_URL=postgresql://postgres:password@db:5432/expense_bot
TELEGRAM_TOKEN=tu_token_de_botfather
WEBHOOK_URL=   # Vacío en local, URL pública de Railway en producción
```

---

## 🗃️ Modelo de base de datos

```
expenses
├── id           — identificador único
├── chat_id      — ID del usuario en Telegram
├── category     — categoría o descripción del gasto
├── amount       — monto del gasto
└── created_at   — fecha y hora del registro
```

---

## 💬 Comandos del bot

| Mensaje | Acción |
|---|---|
| `Almuerzo 15000` | Registra un gasto |
| `Transporte 3500` | Registra un gasto |
| `gastos` o `/gastos` | Muestra resumen del mes con total |
| `/borrar` | Elimina todos los gastos del mes actual |

---

## 🚀 Deploy en Railway

### Variables requeridas

```env
DATABASE_URL=    # URL de PostgreSQL en Railway (${{Postgres.DATABASE_URL}})
TELEGRAM_TOKEN=  # Token de BotFather
WEBHOOK_URL=     # URL pública asignada por Railway
```

### Configuración

- **Pre-deploy command:** `alembic upgrade head`
- **Start command:** `uvicorn app.main:app --host 0.0.0.0 --port 8000`

### Verificar webhook activo

```bash
curl https://api.telegram.org/bot<TOKEN>/getWebhookInfo
```

---

## 💡 Aprendizajes clave

- `python-telegram-bot` — handlers, comandos y respuestas asíncronas
- Diferencia entre **polling** (local) y **webhook** (producción)
- Switch automático polling/webhook según variable de entorno
- Docker Compose — múltiples contenedores en red interna compartida
- Diferencia entre `localhost` y nombre de servicio dentro de Docker
- Volúmenes Docker — por qué `docker-compose down -v` limpia los datos
- Parsing de texto libre a datos estructurados

---

---

# 🤖 Expense Bot (English)

---

## 📌 Description

Telegram bot to log and query personal expenses in natural language.
Type `Lunch 15000` and the bot saves the expense to PostgreSQL, shows summaries, and lets you clear the month.
Automatically switches between polling (local) and webhook (Railway production).

Built as part of a Python learning plan focused on backend development.

**GitHub:** https://github.com/SergioArdCr/expense-bot  
**Railway:** https://expense-bot-production-de35.up.railway.app

---

## 🛠️ Tech Stack

| Library | Usage |
|---|---|
| `FastAPI` | Web framework to receive Telegram webhook |
| `python-telegram-bot` | Interaction with Telegram API |
| `SQLAlchemy` | ORM for database management |
| `PostgreSQL` | Expense storage |
| `Alembic` | Database migrations |
| `Docker Compose` | Container orchestration (api + db) |

---

## 📁 Structure

```
expense-bot/
├── app/
│   ├── bot/
│   │   ├── handlers.py         # Telegram message handling
│   │   └── parser.py           # Text to structured data parsing
│   ├── db/
│   │   └── session.py          # PostgreSQL connection
│   ├── models/
│   │   └── expense.py          # Expense model
│   ├── schemas/
│   │   └── expense.py          # Pydantic validation
│   ├── services/
│   │   └── expense_service.py  # CRUD logic
│   └── main.py                 # FastAPI + automatic webhook/polling
├── alembic/                    # Migrations
├── docker-compose.yml
├── Dockerfile
├── .env.example
└── requirements.txt
```

---

## ⚙️ Setup

```bash
# Clone the repository
git clone https://github.com/SergioArdCr/expense-bot.git
cd expense-bot

# Create virtual environment
python -m venv venv
venv\Scripts\activate       # Windows
source venv/bin/activate    # Mac/Linux

# Install dependencies
pip install -r requirements.txt

# Set up environment variables
cp .env.example .env
# Edit .env with your values

# Start containers
docker-compose up --build

# Run migrations
docker-compose exec api alembic upgrade head
```

---

## 🔐 Environment Variables

```env
DATABASE_URL=postgresql://postgres:password@db:5432/expense_bot
TELEGRAM_TOKEN=your_botfather_token
WEBHOOK_URL=   # Empty locally, Railway public URL in production
```

---

## 🗃️ Database Model

```
expenses
├── id           — unique identifier
├── chat_id      — Telegram user ID
├── category     — expense category or description
├── amount       — expense amount
└── created_at   — timestamp
```

---

## 💬 Bot Commands

| Message | Action |
|---|---|
| `Lunch 15000` | Logs an expense |
| `Transport 3500` | Logs an expense |
| `gastos` or `/gastos` | Shows monthly summary with total |
| `/borrar` | Deletes all expenses for the current month |

---

## 🚀 Deploy on Railway

### Required Variables

```env
DATABASE_URL=    # Railway PostgreSQL URL (${{Postgres.DATABASE_URL}})
TELEGRAM_TOKEN=  # BotFather token
WEBHOOK_URL=     # Public URL assigned by Railway
```

### Configuration

- **Pre-deploy command:** `alembic upgrade head`
- **Start command:** `uvicorn app.main:app --host 0.0.0.0 --port 8000`

### Verify active webhook

```bash
curl https://api.telegram.org/bot<TOKEN>/getWebhookInfo
```

---

## 💡 Key Learnings

- `python-telegram-bot` — async handlers, commands and replies
- Difference between **polling** (local) and **webhook** (production)
- Automatic polling/webhook switch via environment variable
- Docker Compose — multiple containers on a shared internal network
- Difference between `localhost` and service name inside Docker
- Docker volumes — why `docker-compose down -v` wipes data
- Free-text parsing into structured data
