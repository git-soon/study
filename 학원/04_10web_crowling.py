from bs4 import BeautifulSoup
import requests


# def get_html(url):
#     response = requests.get(url)
#     html = BeautifulSoup(response.text, 'html.parser')
#     return html

# # 명언 크롤링


# url = "https://quotes.toscrape.com/"
# tell_list = html.selects(".col-md-8 > .quote")
# a = tell_list
# print(a)


url = "https://www.museum.go.kr/MUSEUM/main/index.do"
response = requests.get(url)
html = BeautifulSoup(response.text, 'html.parser')
# print(html)

# html.select('a')
title1 = html.select('strong.info-tit')
print(title1.text)
