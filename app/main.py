from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.routes.payment import router
from app.database import engine
from app.models import Base

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Cashfree Payment API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:3000",
        "https://ubiquitous-system-6x5vg6977j53rrgw-3000.app.github.dev",
        "https://your-vercel-app.vercel.app",  
        "https://mqmclz-3000.csb.app"
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(router)

@app.get("/")
def root():
    return {"status": "Backend running"}
