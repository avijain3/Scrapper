# app/routes.py
from fastapi import APIRouter, HTTPException
from app.scraper import WebScraper
from app.cache import CacheManager
from app.storage import StorageManager

router = APIRouter()

# Initialize cache and storage managers
cache = CacheManager()
storage = StorageManager()

@router.post("/scrape", tags=["Scraping"])
async def scrape(limit: int = 5, proxy: str = None):
    """
    API endpoint to start scraping process.
    - `limit`: Number of pages to scrape (default: 5).
    - `proxy`: Proxy string for scraping (optional).
    """
    scraper = WebScraper(limit=limit, proxy=proxy, cache=cache, storage=storage)
    try:
        result = await scraper.scrape()
        return {
            "status": "success",
            "message": f"Scraped {len(result)} products successfully.",
            "data": result,
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
