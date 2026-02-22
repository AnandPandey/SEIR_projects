#  Project 1: Web Page Similarity using SimHash

##  Objective
The objective of this project is to compare two web pages and determine their similarity using **SimHash**, a technique widely used in search engines for **near-duplicate document detection**.

The project extracts textual content from web pages, computes word frequencies, generates SimHash fingerprints, and compares them using **Hamming distance**.

---

##  Information Retrieval Concepts Used

| Concept | Description |
|------|------------|
| Web Crawling | Fetching live web pages using HTTP requests |
| HTML Parsing | Extracting title, body text, and hyperlinks |
| Tokenization | Manual word extraction (character-based) |
| Term Frequency (TF) | Counting occurrences of words |
| Hashing | Polynomial rolling hash |
| Document Fingerprinting | SimHash |
| Similarity Measure | Hamming Distance |

---

##  Technologies Used
- **Python**
- `requests`
- `BeautifulSoup (bs4)`
- Standard Python libraries (`sys`)

---

##  Working Methodology

1. **Fetch Web Pages**
   - Sends HTTP requests with a custom User-Agent
   - Parses HTML using BeautifulSoup

2. **Text Extraction**
   - Removes `<script>` tags
   - Extracts visible text from the `<body>`
   - Collects all hyperlinks

3. **Tokenization**
   - Converts text to lowercase
   - Extracts alphanumeric words manually

4. **Word Frequency Calculation**
   - Counts frequency of each word in the document

5. **SimHash Generation**
   - Computes a 64-bit SimHash using word frequencies

6. **Similarity Computation**
   - Uses XOR to compute differing bits
   - Calculates number of common bits
