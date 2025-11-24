#main.py
from fastapi import FastAPI
from app.Mail.controller import router as mail_router

app = FastAPI()

app.include_router(mail_router, prefix="/mail", tags=["mail"])
@app.get("/")
async def root():
    return {"message": "Welcome to BlondeMail API"}
 