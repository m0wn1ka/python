a="""            ___                __ _         
            / _ \              /_ | |        
  _ __ ___ | | | |_      ___ __ | | | ____ _ 
 | '_ ` _ \| | | \ \ /\ / / '_ \| | |/ / _` |
 | | | | | | |_| |\ V  V /| | | | |   < (_| |
 |_| |_| |_|\___/  \_/\_/ |_| |_|_|_|\_\__,_|"""
print(a)


#ref site  https://realpython.com/python-web-scraping-practical-introduction/
from datetime import date
from bs4 import BeautifulSoup
from urllib.request import urlopen
import csv
#url="https://www.thehindu.com/news/international"
#url="https://timesofindia.indiatimes.com/world"
url="https://www.eenadu.net/world"
page=urlopen(url)
html=page.read().decode('utf-8')
soup=BeautifulSoup(html,'html.parser')
news1=soup.find_all("h3",class_="fnt20 article-title-rgt")
with open("today.txt","a") as  f:
	f.write(str(date.today()))
	f.write("\n")
	for i in news1:

		f.write(i.text)
		print(i.text)
		f.write("\n")
