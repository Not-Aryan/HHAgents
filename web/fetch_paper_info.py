# filename: fetch_paper_info.py

import requests
from bs4 import BeautifulSoup

url = "https://arxiv.org/abs/2308.08155"

response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

title = soup.find('h1', class_='title mathjax').text.replace('Title: ', '')
authors = soup.find('div', class_='authors').text.replace('Authors:', '')
abstract = soup.find('blockquote', class_='abstract mathjax').text.replace('Abstract:  ', '')

print(f"Title: {title}\n")
print(f"Authors: {authors}\n")
print(f"Abstract: {abstract}\n")