import sys
import requests
from bs4 import BeautifulSoup

def get_page_data(url):
    response = requests.get(url, headers={"User-Agent": "StudentProject/1.0"})
    if response.status_code != 200:
        print("Failed to fetch:", url)
        sys.exit(1)

    soup = BeautifulSoup(response.text, "html.parser")
    
    if soup.title:
        title = soup.title.get_text(strip=True)
    else:
        title = "No title"

    for s in soup.find_all("script"):
        s.decompose()

    if soup.body:
        body_text = soup.body.get_text(" ", strip=True)
    else:
        body_text = ""

    links = []
    for a in soup.find_all("a"):
        href = a.get("href")
        if href:
            links.append(href)

    return title, body_text, links


if len(sys.argv) != 2:
    print("Usage: python scraper.py url")
    sys.exit(1)

url = sys.argv[1]
title, body_text, links = get_page_data(url)
print()
print("TITLE: ", title)
print()
print("BODY_TEXT: ", body_text)
print()
print("OUTLINKS:")
for link in links:
    print(link)
