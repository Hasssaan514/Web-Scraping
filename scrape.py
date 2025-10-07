from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import re
import time

def scrape_website(website):
    print("Launching web browser...")

    chrome_driver_path = r"C:\Users\HIqbal\OneDrive - Cedar Financial\Documents\VS code projects\PracticeExs\WebScraping1\chromedriver.exe"

    options = webdriver.ChromeOptions()
    driver = webdriver.Chrome(service=Service(chrome_driver_path), options=options)

    try:
        # Ensure website has http/https
        if not website.startswith("http://") and not website.startswith("https://"):
            website = "https://" + website

        driver.get(website)
        print("Successfully launched web browser...")
        time.sleep(5)

        html = driver.page_source
        return html

    finally:
        driver.quit()
