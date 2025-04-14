
#  AI Web Scraper with Streamlit, Selenium & LLM Parsing

This project is an AI-powered web scraper that:

- Uses Selenium to scrape websites (even those with captchas).
- Extracts and cleans the DOM content.
- Sends the cleaned content to an LLM (Llama2 via Ollama) for parsing based on user-defined instructions.

##  Features

-  Scrapes any publicly accessible website
-  Bypasses simple captchas using Scraping Browser's API
-  Extracts and cleans body content with BeautifulSoup
-  Parses content using LLM (Ollama + Llama2)
-  Custom parsing based on user input
-  Streamlit web interface


##  Requirements

Make sure you have the following installed:

- Python 3.8+
- Ollama with Llama2 model installed
- Scraping Browser Remote WebDriver URL (e.g., from ScrapingBrowser)
- Chrome and ChromeDriver installed (chromedriver must match your Chrome version)

Install required packages:

```bash
pip install -r requirements.txt
```
requirements.txt should include:


streamlit
selenium
python-dotenv
beautifulsoup4
langchain
langchain_ollama

## Project stucture


├── main.py            # Streamlit interface
├── scrape.py          # Web scraping logic
├── parse.py           # LangChain + Ollama parsing logic
├── .env               # Contains your WebDriver endpoint
├── chromedriver.exe    # ChromeDriver executable
└── README.md


## Setup

Add you WebDriver URL in `.env`:

```bash
SBR_WEBDRIVER=https://your-sbr-webdriver-endpoint

```

Run The App
```bash

streamlit run main.py
```

##  How to Use

1. Enter the URL of the website you want to scrape.
2. Click "Scrape Site".
3. Enter a custom description of the content you want parsed (e.g., "extract all job titles and company names").
4. Click "Parse Content" to get the structured output using LLM.

##  Example Parse Descriptions

- "Extract all product names and prices"
- "Get all article titles from this blog"
- "List the job titles and company names"

##  Environment Variables

Create a `.env` file in the root directory:


