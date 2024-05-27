from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import time
import pandas as pd
driver=webdriver.Chrome()
driver.get("https://www.sih.gov.in/sih2023-screening-result-batch5")
driver.maximize_window()
table=driver.find_element(By.XPATH,'//*[@id="sheet0"]')

table_html = table.get_attribute('outerHTML')
# Convert the HTML table to a Pandas DataFrame
df = pd.read_html(table_html)[0]

# Save the DataFrame to an Excel file
df.to_excel('batch-5.xlsx', index=False)

# Close the browser window
driver.quit()

print('Table copied to Excel successfully using Selenium.')