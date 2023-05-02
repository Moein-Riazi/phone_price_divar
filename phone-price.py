import requests
from bs4 import BeautifulSoup
import re
from urllib.request import urlopen
import sqlite3

brand = ['apple','samsung','xiaomi']
models_samsumg = {1:'samsung-galaxy-a53-5g',2:'samsung-galaxy-a72-5g',3:'samsung-galaxy-s21',4:'samsung-galaxy-s20'}
models_apple = {1:'apple-iphone-11',2:'apple-iphone-11-pro',3:'apple-iphone-11-pro-max'}
#'''program works well but it needs to be complete in cities and models of brands'''
conn = sqlite3.connect('phone_price.db')
cursor = conn.cursor()
table = """CREATE TABLE phones(name VARCHAR(255),price INT(10),description VARCHAR(255),url VARCHAR(255));"""
cursor.execute(table)

url = "https://divar.ir/s/qom/mobile-phones/samsung/samsung-galaxy-a53-5g?goods-business-type=all"
page = urlopen(url)
html_bytes = page.read()
html = html_bytes.decode("utf-8")
with open("test.txt","w+",encoding='utf-8') as f:
    f.write(html)

with open('test.txt', 'r') as f:
    lines = f.readlines()

with open('test.txt','w+') as f:
    f.seek(0)
    f.writelines(lines[100:])

with open('test.txt') as f:
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