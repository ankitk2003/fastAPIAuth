\# fastAPIAuth

A clean, secure **FastAPI** authentication system with API key support, designed to be plug-and-play and database-agnostic (SQLite, PostgreSQL, MongoDB).

---

## 🔑 Features

- ✅ API key-based authentication via headers or query parameters
- 🔐 Secure endpoints using FastAPI's dependency injection (`Depends`)
- 🧾 Create, renew, revoke API keys and view usage logs
- 🗂️ Supports SQLite (default), PostgreSQL, and partial MongoDB
- 🕒 Automatically expires API keys after 15 days (configurable)
- 🔐 Master secret protection for admin-only endpoints
---

## 🚀 Installation

Install via pip:

```bash
pip install fastapi_auth2


git clone https://github.com/ankitk2003/fastAPIAuth.git
cd fastAPIAuth
poetry install


from fastapi import Depends, FastAPI
from fastapi_auth import api_key_router, api_key_security

app = FastAPI(title="fastAPIAuth Example")

# Include authentication routes
app.include_router(api_key_router, prefix="/auth", tags=["auth"])

# Public route
@app.get("/public")
def public_endpoint():
    return {"msg": "Open to everyone"}

# Protected route
@app.get("/private", dependencies=[Depends(api_key_security)])
def private_endpoint():
    return {"msg": "Protected: valid API key required"}

uvicorn your_module:app --reload


| Variable                            | Default                     | Description                             |
| ----------------------------------- | --------------------------- | --------------------------------------- |
| `FASTAPI_AUTH_SECRET`               | Auto-generated              | Master key for managing API keys        |
| `FASTAPI_AUTH_HIDE_DOCS`            | `False`                     | Hide docs for tombstoned endpoints      |
| `FASTAPI_AUTH_DB_LOCATION`          | `sqlite.db`                 | Path to SQLite database                 |
| `FASTAPI_AUTH_AUTOMATIC_EXPIRATION` | `15` (days)                 | API key expiry duration                 |
| `DATABASE_MODE`                     | `"sqlite"`                  | Use `"postgres"` or `"mongodb"` as well |
| `URI`                               | (Only for Postgres/MongoDB) | e.g. `postgresql://user:pass@host/db`   |
