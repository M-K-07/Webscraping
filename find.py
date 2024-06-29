from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
item="headphones"
file_no= 0
for page in range (0,5):
    driver.get(f"https://www.amazon.in/s?k={item}&page={page}&crid=1RX9B2Y19OZKP&sprefix=hea%2Caps%2C323&ref=nb_sb_ss_pltr-sample-20_1_3")
    time.sleep(3)
    
    elems = driver.find_elements(By.CLASS_NAME, "puis-card-container")
    for elements in elems:
        data=elements.get_attribute("outerHTML")
        with open(f"Items_raw/{item}_{file_no}.html","w",encoding="utf-8") as f:
            f.write(data)
            file_no+=1
driver.close()