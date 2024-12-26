class WebScraper:
    def __init__(self, limit: int = 5, proxy: str = None, cache: CacheManager = None, storage: StorageManager = None):
        self.limit = limit
        self.proxy = proxy
        self.base_url = "https://dentalstall.com/shop/"
        self.headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"}
        self.cache = cache or CacheManager()
        self.storage = storage or StorageManager()

    async def scrape(self) -> List[Dict]:
        products = []
        for page in range(1, self.limit + 1):
            cache_key = f"products_page_{page}"
            cached_data = self.cache.get(cache_key)

            if cached_data:
                print(f"Cache hit for page {page}")
                products.extend(cached_data)
                continue

            url = f"{self.base_url}?page={page}"
            print(f"Scraping URL: {url}")
            response = self._fetch_page(url)
            if not response:
                continue

            page_products = self._parse_page(response.text)
            self.cache.set(cache_key, page_products, ttl=3600)
            products.extend(page_products)

        self._store_to_db(products)
        return products

    def _fetch_page(self, url: str):
        """
        I have taken 3 retries, with a time difference of 5 seconds between each 
        """
        retry_attempts = 3
        for attempt in range(retry_attempts):
            try:
                proxies = {"http": self.proxy, "https": self.proxy} if self.proxy else None
                response = requests.get(url, headers=self.headers, proxies=proxies, timeout=10)
                response.raise_for_status()
                return response
            except requests.RequestException as e:
                print(f"Error fetching URL {url}: {e}. Retrying ({attempt + 1}/{retry_attempts})...")
                sleep(5)
        return None

    def _parse_page(self, html: str) -> List[Dict]:
    soup = BeautifulSoup(html, "html.parser")
    products = []

    # Update selector based on actual class names
    for product in soup.select("li.product"):  # Assuming product container is 'li' with class 'product'
        title = (
            product.select_one("h2.woocommerce-loop-product__title").get_text(strip=True)
            if product.select_one("h2.woocommerce-loop-product__title") else "Unknown"
        )
        price = (
            product.select_one("span.woocommerce-Price-amount").get_text(strip=True)
            if product.select_one("span.woocommerce-Price-amount") else "0"
        )
        image_tag = product.select_one("img")
        image_url = image_tag["src"] if image_tag else ""

        products.append({
            "product_title": title,
            "product_price": price,
            "image_url": image_url
        })

    return products


        return products

    def _store_to_db(self, products: List[Dict]):
        self.storage.save(products)
        print(f"Scraped {len(products)} products and updated the database.")
