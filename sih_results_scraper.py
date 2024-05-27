from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import pandas as pd
import time

# Define URLs to scrape
urls = [
    "https://www.sih.gov.in/sih2023-screening-result-batch1",
    "https://www.sih.gov.in/sih2023-screening-result-batch2",
    "https://www.sih.gov.in/sih2023-screening-result-batch3",
    "https://www.sih.gov.in/sih2023-screening-result-batch4",
    "https://www.sih.gov.in/sih2023-screening-result-batch5"
]

# Create a webdriver instance
driver = webdriver.Chrome()

# Iterate over each URL
for idx, url in enumerate(urls, start=1):
    print(f"Scraping data from {url}")
    
    # Navigate to the URL
    driver.get(url)
    driver.maximize_window()
    time.sleep(5)  # Add a short delay to allow the page to load
    
    # Find the table element
    table = driver.find_element(By.XPATH, '//*[@id="sheet0"]')

    # Get the HTML content of the table
    table_html = table.get_attribute('outerHTML')

    # Convert the HTML table to a Pandas DataFrame
    df = pd.read_html(table_html)[0]

    # Save the DataFrame to an Excel file
    filename = f"batch-{idx}.xlsx"
    df.to_excel(filename, index=False)
    
    print(f"Table from {url} saved as {filename}")

# Close the browser window
driver.quit()

print('All tables copied to Excel successfully using Selenium.')
