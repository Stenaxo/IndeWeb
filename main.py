from crawler import crawl
from database import create_database

if __name__ == "__main__":
    create_database()
    start_url = "https://ensai.fr/"
    crawled = crawl(start_url)
    print(f"URLs Crawled: {len(crawled)}")
