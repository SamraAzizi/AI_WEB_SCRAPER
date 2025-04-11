import selenium.webdrver as webdriver
from selenium.webdriver.chrome.service import Service

def scrape_website(website):
    print("Launchig chrome browser...")

    chrome_driver_path = ""
    options = webdriver.ChromeOption()
    driver = webdriver.Chrome(service=Service(chrome_driver_path), options=options)

    try:
        driver.get(website)
        print("Page Loaded...")
        html = driver.page_source

        return html
    finally:
        driver.quit()
