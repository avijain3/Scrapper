# app/main.py
from fastapi import FastAPI, Depends
from app.auth import verify_token
from app.routes import router

app = FastAPI(title="Web Scraper API", version="1.0.0")

# Health-check endpoint
@app.get("/health", tags=["Health"])
def health_check():
    return {"status": "OK"}

# Add API routes
app.include_router(router, dependencies=[Depends(verify_token)])

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("app.main:app", host="127.0.0.1", port=8000, reload=True)



