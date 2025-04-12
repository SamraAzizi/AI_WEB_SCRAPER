
from selenium.webdriver import Remote, ChromeOptions
from selenium.webdriver.chromium.remote_connection import ChromiumRemoteConnection
from bs4 import BeautifulSoup
from dotenv import load_dotenv
import os

load_dotenv()

SBR_WEBDRIVER = os.getenv("SBR_WEBDRIVER")



def scrape_website(website):
    print("Connecting to Scraping Browser...")
    sbr_connection = ChromiumRemoteConnection(SBR_WEBDRIVER, "goog", "chrome")
    with Remote(sbr_connection, options=ChromeOptions()) as driver:
        driver.get(website)
        print("Waiting captcha to solve...")
        solve_res = driver.execute(
            "executeCdpCommand",


import selenium.webdrver as webdriver
from selenium.webdriver.chrome.service import Service
import time

def scrape_website(website):
    print("Launchig chrome browser...")

    chrome_driver_path = "./chromedriver.exe"
    options = webdriver.ChromeOption()
    driver = webdriver.Chrome(service=Service(chrome_driver_path), options=options)

 
