
# 🕷️ AI Web Scraper with Streamlit, Selenium & LLM Parsing

This project is an AI-powered web scraper that:

- Uses Selenium to scrape websites (even those with captchas).
- Extracts and cleans the DOM content.
- Sends the cleaned content to an LLM (Llama2 via Ollama) for parsing based on user-defined instructions.

## 📦 Features

- 🌐 Scrapes any publicly accessible website
- 🔒 Bypasses simple captchas using Scraping Browser's API
- 🧹 Extracts and cleans body content with BeautifulSoup
- 🤖 Parses content using LLM (Ollama + Llama2)
- 🧠 Custom parsing based on user input
- 🖼️ Streamlit web interface


## 🧰 Requirements

Make sure you have the following installed:

- Python 3.8+
- Ollama with Llama2 model installed
- Scraping Browser Remote WebDriver URL (e.g., from ScrapingBrowser)
- Chrome and ChromeDriver installed (chromedriver must match your Chrome version)

Install required packages:

```bash
pip install -r requirements.txt
```
