import time
import concurrent.futures
from utils import get_sitemap_urls, get_links, can_fetch
from database import save_to_database

import time
from utils import get_sitemap_urls, get_links, can_fetch
from database import save_to_database

def fetch_page(url, crawled_urls):
    if url and can_fetch(url):
        crawled_urls.add(url)
        save_to_database(url)
        links, _ = get_links(url)
        time.sleep(5)  # Attente de cinq secondes
        return links[:5]  # Limite à 5 liens par page
    return []

def crawl(start_url, max_urls=50):
    crawled_urls = set()
    urls_to_crawl = set(get_sitemap_urls(start_url))

    if not urls_to_crawl:
        urls_to_crawl = {start_url}

    while urls_to_crawl and len(crawled_urls) < max_urls:
        url = urls_to_crawl.pop()
        links = fetch_page(url, crawled_urls)
        for link in links:
            if link not in crawled_urls and len(crawled_urls) < max_urls:
                urls_to_crawl.add(link)

    print("Écriture des URLs dans le fichier...")
    with open('crawled_webpages.txt', 'w') as file:
        for url in crawled_urls:
            file.write(url + "\n")

    return crawled_urls

