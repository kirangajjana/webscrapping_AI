import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import logging
import os

# Configure the logging
logging.basicConfig(filename='scraper_log.txt', level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

# Create a new instance of the Microsoft Edge driver
logging.info("Creating Edge WebDriver instance")
driver = webdriver.Edge(options=webdriver.EdgeOptions())

# Read URLs from the "filtered_hyperlinks.txt" file
with open("filtered_hyperlinks.txt", "r") as f:
    urls = f.readlines()

# Create a folder for hyperlinks if it doesn't exist
hyperlink_folder = "Hyperlinkfolder"
if not os.path.exists(hyperlink_folder):
    os.makedirs(hyperlink_folder)

# Iterate through the URLs and scrape each linked page
for url in urls:
    url = url.strip()  # Remove leading/trailing whitespace
    
    # Sanitize the URL to create a valid file name
    filename = url.replace("https://", "").replace("/", "_").replace(".", "_").replace("-", "_").replace(":", "_")
    
    # Load the web page in Selenium
    logging.info(f"Loading web page in Selenium: {url}")
    driver.get(url)

    # Locate and click the first button by its class name if it exists
    first_button_class_name = "ms-Button--action"  # The class name associated with the first button
    try:
        first_button = WebDriverWait(driver, 15).until(EC.element_to_be_clickable((By.CLASS_NAME, first_button_class_name)))
        logging.info(f"Located and clicked the first button with class name: {first_button_class_name}")
        first_button.click()
    except Exception as e:
        logging.warning(f"Failed to locate and click the first button: {str(e)}")
        print("Warning: Failed to locate and click the first button")

    # Locate and click the second button by its class name if it exists
    second_button_class_name = "ms-ExpanderHeader-expand"  # The class name associated with the second button
    try:
        second_button = WebDriverWait(driver, 15).until(EC.element_to_be_clickable((By.CLASS_NAME, second_button_class_name)))
        logging.info(f"Located and clicked the second button with class name: {second_button_class_name}")
        second_button.click()
    except Exception as e:
        logging.warning(f"Failed to locate and click the second button: {str(e)}")
        print("Warning: Failed to locate and click the second button")

    # Wait for a moment to allow the content to load (adjust the sleep time as needed)
    time.sleep(15)
    logging.info("Waiting for content to load (15 seconds)")

    # Scrape all the data text on the web page
    logging.info("Scraping all data text from the page")
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    all_text = soup.get_text()
    
    # Save the scraped data to a file named after the sanitized URL
    with open(f"{filename}_all_data.txt", "w", encoding='utf-8') as f:
        f.write(all_text)
    
    logging.info(f"Saved all data text from {url} to {filename}_all_data.txt")

    # Scrape hyperlinks from the page
    logging.info("Scraping hyperlinks from the page")
    hyperlinks = driver.find_elements(By.TAG_NAME, "a")
    
    # Save hyperlinks as a separate file in the Hyperlinkfolder
    with open(os.path.join(hyperlink_folder, f"{filename}_hyperlinks.txt"), "w") as f:
        for hyperlink in hyperlinks:
            href = hyperlink.get_attribute("href")
            f.write(href + "\n")
    
    logging.info(f"Saved hyperlinks from {url} to {filename}_hyperlinks.txt")

# Close the Selenium WebDriver
logging.info("Closing the Selenium WebDriver")
driver.quit()