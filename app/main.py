from fastapi import FastAPI
from app.routes.payment import router
from app.database import engine
from app.models import Base

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Cashfree Payment API")

app.include_router(router)

@app.get("/")
def root():
    return {"status": "Backend running"}
