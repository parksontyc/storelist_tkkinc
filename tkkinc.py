import requests
from bs4 import BeautifulSoup
import time 
import csv

store_name = []
store_address = []


url = "https://www.tkkinc.com.tw/accessResults.html?city=&area=&attr=&type=1"

res = requests.get(url, timeout=5)

html = res.text

soup = BeautifulSoup(html.replace("\n", "").strip(), "html.parser")

items = soup.find_all("div", class_="access--caption")



for data in items:
	store_name.append(data.h2.text.strip())
	add =data.p.text

	store_address.append(add[3:])

	print(store_name, store_address)


with open('shop_list_tkkinc.csv', 'w', newline='',  encoding="utf-8") as csvfile:
    csvwriter = csv.writer(csvfile, delimiter=',')
    newrow = ['門市名稱', '門市地址']
    csvwriter.writerow(newrow)
    for n in range(0, len(store_name)):
        newrow.clear()
        newrow.append(store_name[n])
        newrow.append(store_address[n])
        
        csvwriter.writerow(newrow)