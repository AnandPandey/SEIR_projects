import sys
import requests
from bs4 import BeautifulSoup

# Creating Function that takes url from command line and extracts title, body text and outlinks for that url
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

# Checking if not valid command line argument 
if len(sys.argv) != 2:
    print("Usage: python scraper.py url")
    sys.exit(1)

url = sys.argv[1]       # Taking url from command line argument
title, body_text, links = get_page_data(url)       # Extracting Page Title, Page Body Text and Page Outlinks
print()
print("TITLE: ", title)       # Prints Title
print()
print("BODY_TEXT: ", body_text)        # Prints Body Text
print()
print("OUTLINKS:")             
for link in links:          
    print(link)            # Prints Outlinks (one per line)

