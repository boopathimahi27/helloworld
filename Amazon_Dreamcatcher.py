# Amazon
from selenium  import webdriver
from bs4 import BeautifulSoup as BeautifulSoup
import pandas as pd

driver = webdriver.Chrome('C:\Driver\chromedriver.exe')
Productname = []
Price = []

driver.get('https://www.amazon.in/s?k=dreamcatcher+white&crid=3P5FU0JW9ZGGJ&sprefix=Dreamcatcher%2Caps%2C427&ref=nb_sb_ss_ts-doa-p_4_12')
content = driver.page_source #Page's  HTML code
soup = BeautifulSoup(content)
for i in soup.find_all('div' , {'class':'a-section a-spacing-medium'}):
    name = i.find('span', attrs = {'class':'a-size-base-plus a-color-base a-text-normal'})
    price = i.find('span', attrs = {'class':'a-price-whole'}) 
    if price:
        Price.append(price.text)
        Productname.append(name.text)        
df = pd.DataFrame({'Product Name': Productname,'Price':Price})
df.to_csv('Dreamcatcher.csv', index = False, encoding = 'utf-8-sig')
