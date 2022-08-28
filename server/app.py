from fastapi import FastAPI
from server.config.settings import apisettings as settings
from server.routes.user import router as user_router
from server.routes.register import router as register_router
from server.routes.auth import router as auth_router
from server.config.database import init_db
from server.utils import jwt

app = FastAPI(
    title=settings.title
)


@app.get('/')
async def root():
    return 'This works!!'


@app.on_event("startup")
async def app_init():
    await init_db()


app.include_router(user_router)
app.include_router(register_router)
app.include_router(auth_router)

