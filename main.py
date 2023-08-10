import uvicorn
from fastapi import FastAPI
from app.routes.api import router as api_router

app = FastAPI()
origins = ["http://localhost:8080"]

app.include_router(api_router, prefix="/api/v1")

if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", reload=True, port=8080, log_level="info")
    print("running...")