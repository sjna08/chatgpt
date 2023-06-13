# 필요한 라이브러리를 임포트합니다.
import streamlit as st
import requests
from bs4 import BeautifulSoup

def scrape_chosun():
    # 조선일보 사설 메인 페이지 URL
    url = 'https://www.chosun.com/opinion'

    # 웹페이지를 가져옵니다.
    response = requests.get(url)

    # BeautifulSoup 객체를 생성합니다.
    soup = BeautifulSoup(response.text, 'html.parser')

    # 뉴스 기사 제목과 링크를 포함한 HTML 요소를 가져옵니다.
    articles = soup.find_all('h3', class_='gs-c-promo-heading__title gel-pica-bold nw-o-link-split__text')

    # 각 기사의 제목과 링크를 출력합니다.
    for article in articles:
        title = article.text
        link = article.find_parent('a')['href']
        if not link.startswith('http'):
            link = 'https://www.chosun.com' + link
        st.write(f'Title: {title}, Link: {link}')

# 스트림릿 앱을 실행합니다.
def run():
    st.title("조선일보 사설")
    scrape_chosun()

if __name__ == '__main__':
    run()
