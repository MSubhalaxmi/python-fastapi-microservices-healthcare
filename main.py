from fastapi import FastAPI
from app.api.routes import router
from app.db.database import database

app = FastAPI(title="Clinical Data Service")

@app.on_event("startup")
async def startup():
    await database.connect()

@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()

app.include_router(router)

@app.get("/")
def health_check():
    return {"status": "Service Running"}