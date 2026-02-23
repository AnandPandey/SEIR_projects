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


def get_words(text):
    text = text.lower()
    words = []
    curr_word = ""
    for ch in text:
        if ch.isalnum():
            curr_word += ch
        else:
            if curr_word != "":
                words.append(curr_word)
                curr_word = ""
    if curr_word != "":
        words.append(curr_word)
    return words
    

def word_freq(text):
    words = get_words(text)
    freq = {}
    for word in words:
        if word in freq:
            freq[word] += 1
        else:
            freq[word] = 1
    return freq
    

def word_hash(word):
    p = 53
    m = 2**64
    hash = 0
    pow = 1
    for ch in word:
        hash = (hash + ord(ch) * pow) % m
        pow = (pow * p) % m
    return hash
    

def simhash(freq):
    bits = [0] * 64
    for word in freq:
        hash = word_hash(word)
        count = freq[word]
        
        for i in range(64):
            bit = (hash >> i) & 1
            if bit == 1:
                bits[i] = bits[i] + count
            else:
                bits[i] = bits[i] - count

    sim_hash_val = 0
    for i in range(64):
        if bits[i] > 0:
            sim_hash_val = sim_hash_val + (1 << i)
    return sim_hash_val
    

def common_bits(hash1, hash2):
    x = hash1 ^ hash2
    count = 0
    for i in range(64):
        if x & 1 == 1:
            count += 1
        x = x >> 1
    return 64 - count
    
    
if len(sys.argv) != 3:
    print("Usage: python script.py url1 url2")
    sys.exit(1)

url1 = sys.argv[1]
url2 = sys.argv[2]

title1, text1, links1 = get_page_data(url1)
title2, text2, links2 = get_page_data(url2)

print("TITLE 1:", title1)
print("TITLE 2:", title2)
print()
print("TEXT 1:", text1)
print()
print("TEXT 2:", text2)
print()
print("LINKS IN URL 1:", links1)
print()
print("LINKS IN URL 2:", links2)

freq1 = word_freq(text1)
freq2 = word_freq(text2)

hash1 = simhash(freq1)
hash2 = simhash(freq2)
print()
print("Common bits in simhashes:", common_bits(hash1, hash2))
print()


