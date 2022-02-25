import os 
from selenium import webdriver
import csv

driver = webdriver.Chrome()
driver.get("https://www.ebay.com/sch/i.html?_from=R40&_nkw=macbook&_sacat=0&_oaa=1&_dcat=111422&rt=nc&LH_ItemCondition=3000")

all_titles = []

all_items = driver.find_elements_by_xpath('//h3[@class="s-item__title"]')

for item in all_items:
    title = item.text.strip()
    print('title:', title)
    all_titles.append( title )

all_prices = []

all_items = driver.find_elements_by_xpath('//span[@class="s-item__price"]')

for item in all_items:
    price = item.text.strip()
    print('price:', price)
    all_prices.append( price )

data = list(zip(all_titles, all_prices))

all_others = []

all_items = driver.find_elements_by_xpath('//non_existing_xpath')

for item in all_items:
    other = item.text.strip()
    print('other:', other)
    all_others.append( other )

with open('GFG', 'w') as f:
    write = csv.writer(f)

    #write.writerow()
    write.writerows(data)
