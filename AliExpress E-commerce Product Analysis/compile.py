from bs4 import BeautifulSoup
import pandas as pd
import os

products_data = []
for file in os.listdir("Work/data/"): #add folder path here
    try:
        with open(f"Work/data/{file}") as f: #add folder path here
            html_doc=f.read()
        soup = BeautifulSoup(html_doc, 'html.parser')
        title=soup.h3.get_text().replace("\n       ","").strip()
        try:
            curr_price= soup.find('div', class_='kr_kj').get_text()
        except:
            curr_price = 'N/A'
        
        try:
            orig_price=soup.find('div', class_='kr_kk').get_text()
        except:
            orig_price='N/A'
        
        try:
            discount=soup.find('span', class_='kr_lk').get_text()
        except:
            discount= 'N/A'

        try:
            shipping_info=soup.find('div', class_='kr_ls').get_text()
        except:
            shipping_info='N/A'
        
        product = {
        'Title': title,
        'Curr_price': curr_price,
        'Orig_price': orig_price,
        'Discount':discount,
        'Shipping_info':shipping_info
        }
        
        products_data.append(product)
        print(products_data)
    except Exception as ex:
        print(ex) 

#Create the DataFrame from the list of dictionaries
df = pd.DataFrame(products_data)
df.to_csv("Wor/data/data.csv") #Add folder path here
