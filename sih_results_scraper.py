from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import pandas as pd
import time

urls = [
    "https://www.sih.gov.in/sih2023-screening-result-batch1",
    "https://www.sih.gov.in/sih2023-screening-result-batch2",
    "https://www.sih.gov.in/sih2023-screening-result-batch3",
    "https://www.sih.gov.in/sih2023-screening-result-batch4",
    "https://www.sih.gov.in/sih2023-screening-result-batch5"
]

driver = webdriver.Chrome()

for idx, url in enumerate(urls, start=1):
    print(f"Scraping data from {url}")
    
    driver.get(url)
    driver.maximize_window()
    time.sleep(5) 
    
    table = driver.find_element(By.XPATH, '//*[@id="sheet0"]')

    table_html = table.get_attribute('outerHTML')

    
    df = pd.read_html(table_html)[0]

    
    filename = f"batch-{idx}.xlsx"
    df.to_excel(filename, index=False)
    
    print(f"Table from {url} saved as {filename}")


driver.quit()

print('All tables copied to Excel successfully using Selenium.')
