import pandas as pd
from bs4 import BeautifulSoup
import os
data= {"Item":[],"Price":[],"Link":[]}
try:
    for file in os.listdir('Items_raw'):
        with open(f"Items_raw/{file}") as f:
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
        
df=pd.DataFrame(data=data)
df.to_csv("items_list.csv")
    
    