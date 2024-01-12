import requests ## 요청 라이브러리
from bs4 import BeautifulSoup #파싱 라이브러리

url = 'https://ridibooks.com/category/new-releases/2200'
response = requests.get(url)
response.encoding = 'utf-8'
html = response.text

soup = BeautifulSoup(html, 'html.parser') # html 파서 씀

bookservices = soup.select('.title_text') # 클래스 짚어내기
for no, book in enumerate(bookservices, 1):
    print(no, book.text.strip())