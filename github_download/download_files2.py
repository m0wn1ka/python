import requests
from bs4 import BeautifulSoup

#url = "https://raw.githubusercontent.com/m0wn1ka/m0wn1ka.github.io/main/index.html"
url="https://github.com/m0wn1ka/m0wn1ka.github.io/tree/main/assets/img/certificates"
response = requests.get(url)

if response.status_code == 200:
    html = response.text
    soup = BeautifulSoup(html, 'html.parser')
    news1 = soup.find_all("a", class_="Link--primary")

    for link in news1:
        print(link['href'])
else:
    print(f"Failed to retrieve content. Status code: {response.status_code}")
