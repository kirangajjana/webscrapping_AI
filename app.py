import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import logging

# Configure the logging
logging.basicConfig(filename='scraper_log.txt', level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

# Define the URL of the web page you want to scrape
url = "url"

# Create a new instance of the Microsoft Edge driver
logging.info("Creating Edge WebDriver instance")
driver = webdriver.Edge(options=webdriver.EdgeOptions())

# Load the web page in Selenium
logging.info(f"Loading web page in Selenium: {url}")
driver.get(url)

# Locate and click the first button by its class name
first_button_class_name = "ms-Button--action"  # The class name associated with the first button
try:
    first_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CLASS_NAME, first_button_class_name)))
    logging.info(f"Located and clicked the first button with class name: {first_button_class_name}")
    first_button.click()
except Exception as e:
    logging.error(f"Failed to locate and click the first button: {str(e)}")
    print("Failed to locate and click the first button:", str(e))

# Wait for a moment to allow the content to load (adjust the sleep time as needed)
time.sleep(2)
logging.info("Waiting for content to load (2 seconds)")

# Locate and click the second button by its class name
second_button_class_name = "ms-ExpanderHeader-expand"  # The class name associated with the second button
try:
    second_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CLASS_NAME, second_button_class_name)))
    logging.info(f"Located and clicked the second button with class name: {second_button_class_name}")
    second_button.click()
except Exception as e:
    logging.error(f"Failed to locate and click the second button: {str(e)}")
    print("Failed to locate and click the second button:", str(e))

# Wait for a moment to allow the content to load (adjust the sleep time as needed)
time.sleep(2)
logging.info("Waiting for content to load (2 seconds)")

# Scrape hyperlinks from the page and save them to a separate file
logging.info("Scraping hyperlinks from the page")
hyperlinks = driver.find_elements(By.TAG_NAME, "a")
with open("hyperlinks.txt", "w") as f:
    for hyperlink in hyperlinks:
        href = hyperlink.get_attribute("href")
        f.write(href + "\n")
        logging.info(f"Found hyperlink: {href}")

# Scrape all the data text on the web page
logging.info("Scraping all data text from the page")
soup = BeautifulSoup(driver.page_source, 'html.parser')
all_text = soup.get_text()
with open("all_data.txt", "w", encoding='utf-8') as f:
    f.write(all_text)
logging.info("Saved all data text to all_data.txt")

# Now, proceed with scraping the collapsible sections (similar to the previous script)

# Identify the collapsible sections and their trigger elements
collapsibles = driver.find_elements(By.CLASS_NAME, "collapsible")  # Locate by class name

# Create a list to store the scraped data
scraped_data = []

# Loop through each collapsible section and extract the data
for i, collapsible in enumerate(collapsibles, start=1):
    # Click the collapsible trigger using Selenium
    collapsible.click()
    logging.info(f"Clicked collapsible section {i}")
    
    # Wait for a moment to allow the content to load (adjust the sleep time as needed)
    time.sleep(2)
    logging.info("Waiting for content to load (2 seconds)")
    
    # Extract the content from the revealed section using BeautifulSoup
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    content = soup.find(class_="content")  # Replace with the actual class name or identifier
    
    # Append the content to the scraped_data list
    scraped_data.append(content.get_text())
    logging.info(f"Scraped content from collapsible section {i}")

# Now, you have the scraped data in the scraped_data list
for i, data in enumerate(scraped_data, start=1):
    logging.info(f"Content from collapsible section {i}:\n{data}")
    print(data)

# Close the Selenium WebDriver
logging.info("Closing the Selenium WebDriver")
driver.quit()
    