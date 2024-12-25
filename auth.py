# app/auth.py
from fastapi import HTTPException, Header

STATIC_TOKEN = "TOKEN_VALUE"

def verify_token(token: str = Header(...)):
    if token != STATIC_TOKEN:
        raise HTTPException(status_code=403, detail="Invalid authentication token")
