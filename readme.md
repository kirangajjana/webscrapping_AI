# Webscrapping
 **This is a script to scrape text data from a website using Selenium and BeautifulSoup, and then storing the scraped data in a CSV file**

## Getting Started
  
  - These instructions will guide you on how to set up and run the web scraping script on your local machine.

## Prerequisites
  > You need to have the following software installed on your machine:
  - Python 3.x
  - Selenium WebDriver
  - Microsoft Edge Browser
  **You also need to install the following Python libraries:**
  - BeautifulSoup
  - requests
  - pandas

  **You can install these libraries using pip:**

  ```python
  pip install beautifulsoup4 requests pandas selenium
```
## Installing
  
   - Clone the GitHub repository to your local machine.
   - Navigate to the directory containing the Python script.
   - Run the Python script using the command python app.py

  - The script uses Selenium to load the webpage and interact with it, and BeautifulSoup to parse the HTML and extract the text data. The script also handles clickable elements on the page that reveal additional content when clicked.

  - The script saves the scraped text data into a pandas DataFrame and then writes the DataFrame to a CSV file.

## Built With
- Python: The programming language used
- Selenium WebDriver: Used to automate browser activities
- BeautifulSoup: Used to parse HTML and extract data
- pandas: Used to store and save the scraped data.
