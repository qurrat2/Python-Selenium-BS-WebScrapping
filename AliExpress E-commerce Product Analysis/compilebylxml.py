from bs4 import BeautifulSoup
import pandas as pd
import os
from lxml import html
from lxml import etree


product_data = []


for file in os.listdir("data/"): #add path here
    try:
        with open(f"{file}") as f: #add path here
            html_doc=f.read()
        soup = BeautifulSoup(html_doc, 'html.parser')
        dom =  etree.HTML(str(soup))
      

        title=dom.xpath('//a/div[2]/div[1]/@title')[0]
       
        try:
            curr_price= ''.join(dom.xpath('//a/div[2]/div[2]/div[1]/span/text()'))
        except:
            curr_price = 'N/A'
      
        try:
            orig_price=dom.xpath('//a/div[2]/div[2]/div[2]/span/text()')[0]
        except:
            orig_price='N/A'
        
        try:
            discount=dom.xpath('//a/div[2]/div[2]/span/text()')[0]
        except:
            discount= 'N/A'

        try:
            shipping_info=dom.xpath('//a/div[2]/div[4]/div[2]/span/@title')[0]
        except:
            shipping_info='N/A'
        
        product = {
        'Title': title,
        'Curr_price': curr_price,
        'Orig_price': orig_price,
        'Discount':discount,
        'Shipping_info':shipping_info
        }
        
        product_data.append(product)
        print(product_data)
      
    except Exception as ex:
        print(ex) 

#Create the DataFrame from the list of dictionaries
df = pd.DataFrame(product_data)
df.to_csv("data/data2.csv") #add path here
