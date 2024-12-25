# Scrapper
A web scrapper written using FAST API for Dentalstall


This project is a web scraping tool built using the FastAPI framework. It automates scraping product information (name, price, and image) from a target website and provides an API to manage and trigger the scraping tasks.

Features
Web Scraping

Scrapes product names, prices, and images from a target website.
Supports limiting the number of pages to scrape.
Optionally uses a proxy for scraping requests.
Data Storage

Stores scraped data locally as a JSON file.
Modular design allows swapping the storage backend (e.g., database).
Caching

Uses Redis for caching scraped results.
Updates only when the product price has changed.
Notifications

Sends notifications (console print in this implementation) about scraping results.
Modular design allows adding other notification strategies (e.g., email, Slack).
Authentication

Secures API endpoints with token-based authentication.
Modular Codebase

Adopts an object-oriented approach for scalability and maintainability.
Separates concerns across distinct modules.
