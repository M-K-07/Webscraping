from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import pandas as pd
from bs4 import BeautifulSoup
import time
import os

# Selenium Driver Reads the Webpage and extracts the all the HTML content of the products to the folder of products name 
item=input("Search products: ")
driver = webdriver.Chrome()
file_no= 0
os.makedirs(f'{item}', exist_ok=True)
try:
    
    for page in range (0,2):
        driver.get(f"https://www.amazon.in/s?k={item}&page={page}&crid=1RX9B2Y19OZKP&sprefix=hea%2Caps%2C323&ref=nb_sb_ss_pltr-sample-20_1_3")
        time.sleep(3)
        
        elems = driver.find_elements(By.CLASS_NAME, "puis-card-container")
        for elements in elems:
            data=elements.get_attribute("outerHTML")
            with open(f"{item}/{item}_{file_no}.html","w",encoding="utf-8") as f:
                f.write(data)
                file_no+=1
    driver.close()
except Exception as e:
    print(e)
    for html_file in os.listdir(item):
        os.remove(os.path.join(item, html_file))
    os.rmdir(item)

# The Product HTML files are read by bs4 and extracts the useful info from the script and createsa a pandas DataFrame and store the extracted data with specified products file name

data= {"Item":[],"Price":[],"Link":[]}
try:
        
    for file in os.listdir(item):
        with open(f"{item}/{file}") as f:
            html_doc= f.read()
        soup = BeautifulSoup(html_doc, 'html.parser')
        
        title=soup.find('h2')
        item_name=title.get_text().strip()
        
        price=soup.find("span", class_="a-price-whole")
        item_price=price.get_text()
        
        link=soup.find("a")
        item_link=f"https://amazon.in/{link['href']}"
        
        data["Item"].append(item_name)
        data["Price"].append(item_price)
        data["Link"].append(item_link)
    
except Exception as e:
    print(e) 
        
for html_file in os.listdir(item):
    os.remove(os.path.join(item, html_file))
os.rmdir(item)

df=pd.DataFrame(data=data)
df.to_excel(f"{item}.xlsx",index=False)
    
    