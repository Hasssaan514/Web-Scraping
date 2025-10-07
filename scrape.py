from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import time
import os
import platform

def scrape_website(website):
    print("Launching web browser...")

    options = Options()
    options.add_argument('--headless')  # Run without GUI
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    options.add_argument('--disable-gpu')
    options.add_argument('--window-size=1920,1080')
    
    # Detect if running locally or in cloud
    if platform.system() == "Windows":
        # Local Windows - use your chromedriver.exe
        chrome_driver_path = "chromedriver.exe"
        driver = webdriver.Chrome(service=Service(chrome_driver_path), options=options)
    else:
        # Cloud/Linux - use system chromedriver
        driver = webdriver.Chrome(options=options)

    try:
        if not website.startswith("http://") and not website.startswith("https://"):
            website = "https://" + website

        driver.get(website)
        print("Successfully launched web browser...")
        time.sleep(5)

        html = driver.page_source
        return html

    finally:
        driver.quit()