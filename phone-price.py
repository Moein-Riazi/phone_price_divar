import requests
from bs4 import BeautifulSoup
import re
from urllib.request import urlopen
import sqlite3
from os import system,environ

system("rm ./*.db 2>/dev/null")

selected_city = environ.get("CITY")
selected_cat = environ.get("CATEGORY")
selected_brand = environ.get("BRAND")
selected_model = environ.get("MODEL")

#print(selected_city,selected_cat,selected_brand,selected_model)
#'''program works well but it needs to be complete in cities and models of brands'''
conn = sqlite3.connect('phone_price.db')
cursor = conn.cursor()
table = """CREATE TABLE phones(name VARCHAR(255),price INT(10),description VARCHAR(255),url VARCHAR(255));"""
cursor.execute(table)

#orginal URL = https://divar.ir/s/qom/mobile-phones/samsung/samsung-galaxy-a53-5g?goods-business-type=all

url = f"https://divar.ir/s/{selected_city}/{selected_cat}/{selected_brand}/{selected_model}?goods-business-type=all"
#print(url)
page = urlopen(url)
html_bytes = page.read()
html = html_bytes.decode("utf-8")
with open("phone_lists.txt","w+",encoding='utf-8') as f:
    f.write(html)

with open('phone_lists.txt', 'r') as f:
    lines = f.readlines()

with open('phone_lists.txt','w+') as f:
    f.seek(0)
    f.writelines(lines[100:])

with open('phone_lists.txt') as f:
    text = f.read()
  
descriptions = re.findall(r'"description":"(.*?)"', text)
prices = re.findall(r'price\":\"(\d+)', text)
names = re.findall(r'"name":"(.*?)"', text)
urls = re.findall(r'"url":"(.*?)"', text)

for i in range(len(names)):
    data = f"INSERT INTO phones VALUES('{names[i]}','{prices[i]}','{descriptions[i]}','{urls[i]}');"
    cursor.execute(data)
                

conn.commit()
conn.close()

print("Well-done!, Operation Done Successful")