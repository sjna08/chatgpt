# 필요한 라이브러리를 임포트합니다.
import streamlit as st
import requests
from bs4 import BeautifulSoup

def scrape_news(url, css_selector):
    # 웹페이지를 가져옵니다.
    response = requests.get(url)

    # BeautifulSoup 객체를 생성합니다.
    soup = BeautifulSoup(response.text, 'html.parser')

    # 뉴스 기사 제목과 링크를 포함한 HTML 요소를 가져옵니다.
    articles = soup.select(css_selector)

    # 각 기사의 제목과 링크를 출력합니다.
    for article in articles:
        title = article.text.strip()
        link = article.get('href')
        if link is not None and not link.startswith('http'):
            link = url + link
        st.write(f'Title: {title}, Link: {link}')

# 스트림릿 앱을 실행합니다.
def run():
    st.title("Korean News Scraper")

    st.write("## 조선일보")
    scrape_news('http://www.chosun.com', '.article-title a')

    st.write("## 매일경제")
    scrape_news('https://www.mk.co.kr', '.tit a')

if __name__ == '__main__':
    run()

    run()
