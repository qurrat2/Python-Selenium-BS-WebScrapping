import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

file=0
query="camera"
driver = webdriver.Chrome()

for i in range(1,6):
    driver.get(f"https://www.aliexpress.us/w/wholesale-{query}.html?page={i}&g=y&SearchText={query}")

    products = driver.find_elements(By.XPATH, "//div[contains(@data-tticheck, 'true')]//a[contains(@href, '/item/')]")
    print(f"{len(products)} products found.")
    
    for product in products:
        d=product.get_attribute("outerHTML")
        with open(f"{query}_{file}.html", "w", encoding="utf-8") as f: #add folder path here
            f.write(d)
            file=file+1

        
    #assert "No results found." not in driver.page_source
   
driver.close()