# app/routes.py
from fastapi import APIRouter, Depends, Query
from app.scraper import WebScraper
from app.storage import JSONStorage

router = APIRouter()

@router.post("/scrape", tags=["Scraping"])
async def scrape(
    limit: int = Query(5, description="Number of pages to scrape"),
    proxy: str = Query(None, description="Proxy string to use"),
):
    scraper = WebScraper(limit=limit, proxy=proxy)
    result = await scraper.scrape()
    storage = StorageManager()
    storage.save(result)
    return {"message": f"{len(result)} products scraped and saved."}
