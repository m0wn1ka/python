from bs4 import BeautifulSoup
from urllib.request import urlopen
import csv
#url="https://www.thehindu.com/news/international"
#url="https://timesofindia.indiatimes.com/world"
#url="https://www.eenadu.net/world"
url="https://github.com/m0wn1ka/m0wn1ka.github.io/tree/main/assets/img/certificates"
page=urlopen(url)
html=page.read().decode('utf-8')
soup=BeautifulSoup(html,'html.parser')
news1=soup.find_all("a",class_="Link--primary")
print("news1",news1)
print("soup is ",soup)
