from fastapi import FastAPI
from sqlmodel import SQLModel

from redirect_manager.api import router as api_router
from redirect_manager.core.database import engine

app = FastAPI()
app.include_router(api_router)


@app.on_event("startup")
async def startup():
    async with engine.begin() as conn:
        await conn.run_sync(SQLModel.metadata.drop_all)
        await conn.run_sync(SQLModel.metadata.create_all)
