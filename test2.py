import requests
from bs4 import BeautifulSoup
import re
from urllib.request import urlopen
import sqlite3

conn = sqlite3.connect('phone_price.db')
cursor = conn.cursor()
table = """CREATE TABLE phones(name VARCHAR(255),price INT(10),description VARCHAR(255),url VARCHAR(255));"""
cursor.execute(table)


#content = requests.get("https://divar.ir/s/qom/mobile-phones/samsung/samsung-galaxy-a53-5g?goods-business-type=all")
#soup = BeautifulSoup(content.text,"html.parser")
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

for name in names:
    for price in prices:
        for description in descriptions:
            for url in urls:
                data = (f"""INSERT INTO phones VALUES('{name}','{price}','{description}','{url}');""")
cursor.execute(data)

conn.commit()
conn.close()