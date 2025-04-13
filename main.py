
import streamlit as st
from scrape import (
    scrape_website,
    split_dom_content,
    clean_body_content,
    extract_body_content,
)

st.title("AI Web Scraper")
url = st.text_input("Enter a website URL: ")

if st.button("Scrape Site"):
    st.write("Scraping the website")
    result = scrape_website(url)
    body_content = extract_body_content(result)
    clean_content = clean_body_content(body_content)
    print(result)

