import time
import urllib.request
from urllib.robotparser import RobotFileParser
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse
from bs4 import BeautifulSoup
import requests

def can_fetch(url, user_agent='*'):
    rp = RobotFileParser()
    rp.set_url(urllib.request.urljoin(url, '/robots.txt'))
    rp.read()
    return rp.can_fetch(user_agent, url)

# utils.py
import urllib.request
import xml.etree.ElementTree as ET

def get_sitemap_urls(url):
    sitemap_url = urllib.request.urljoin(url, '/sitemap.xml')
    try:
        response = urllib.request.urlopen(sitemap_url)
        sitemap = response.read()
        tree = ET.fromstring(sitemap)
        namespaces = {'sitemap': 'http://www.sitemaps.org/schemas/sitemap/0.9'}
        urls = [elem.text for elem in tree.findall('sitemap:url/sitemap:loc', namespaces)]
        return urls
    except Exception as e:
        print(f"Erreur lors de l'accès à {sitemap_url}: {e}")
        return []  # Retourne une liste vide si une exception est levée

def get_links(url):
    try:
        response = requests.get(url)
        html = response.content
        soup = BeautifulSoup(html, 'html.parser')
        links = set()

        for link in soup.find_all('a', href=True):
            href = link.get('href')

            # Ignorer les liens javascript et les ancres
            if href.startswith('#') or href.lower().startswith('javascript:'):
                continue

            # Convertir les liens relatifs en liens absolus
            absolute_link = urljoin(url, href)
            
            # Vérifier si le lien est du même domaine que l'URL d'origine
            if urlparse(absolute_link).netloc == urlparse(url).netloc:
                links.add(absolute_link)

        return list(links)[:5], time.time() - response.elapsed.total_seconds()
    except Exception as e:
        print(f"Erreur lors de l'accès à {url}: {e}")
        return [], 0

