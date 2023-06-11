# !pip install selenium
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

# 크롬드라이버 셋팅
def set_chrome_driver(headless=True):
    options = webdriver.ChromeOptions()
    if headless:
        options.add_argument('headless')
    options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36")
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    return driver
    
# driver 설정
driver = set_chrome_driver(False)
# URL 요청
driver.get(url)

# aritivlePage는 신문기사의 본문입니다
article_page = driver.find_element(By.CLASS_NAME, 'articlePage')
article_page

# 신문기사의 본문을 출력합니다.
print(article_page.text)

# !pip install openai
import openai

# API 키 설정
openai.api_key = "OpenAI API Key 입력"

# 프롬프트 (요약해줘 + 긍/부정 감정도 분석해줘)
prompt = f'''
Summarize the paragraph below and interpret whether it is a positive or negative sentiment.


{article_page.text}
'''
print(prompt)


def summarize(prompt):
    # 모델 엔진 선택
    model_engine = "text-davinci-003"

    # 맥스 토큰
    max_tokens = 3000

    # 요약 요청
    completion = openai.Completion.create(
        engine=model_engine,
        prompt=prompt,
        max_tokens=max_tokens,
        temperature=0.3,       # creativity
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    return completion
    
# 요약 요청후 결과 return
response = summarize(prompt)

# 결과 출력
print(response.choices[0].text)

# 샘플 텍스트
summarized = '''This paragraph is summarizing the current state of the stock market, with the Dow Jones Industrial Average, S&P 500, and NASDAQ Composite all down, while Gold Futures and Advanced Micro Devices Inc (AMD) rose. Investors are cautious ahead of the Federal Reserve's rate decision, and corporate earnings are mixed, with Electronic Arts Inc (EA) and Snap Inc (SNAP) falling and AMD rising. Oil prices are also down. Overall, the sentiment of the paragraph is negative.'''

import time

# 1. 파파고 번역 요청을 위한 selenium 생성
papago = set_chrome_driver(False)
papago.get(f'https://papago.naver.com/')

# 2. 영문 문장 입력
papago.find_element(By.ID, 'txtSource').send_keys(summarized)
# 2. 번역 버튼 클릭
papago.find_element(By.ID, 'btnTranslate').click()

# 강제 지연 시간: 번역을 기다릴 수 있도록 2초 슬립
time.sleep(2)

# 3. 번역된 한글 텍스트 크롤링
papago_translated = papago.find_element(By.ID, 'targetEditArea')
print(papago_translated.text)

def papago_translate(text):
    try:
        papago = set_chrome_driver(False)
        papago.get('https://papago.naver.com/')
        time.sleep(1)
        papago.find_element(By.ID, 'txtSource').send_keys(text)
        papago.find_element(By.ID, 'btnTranslate').click()
        time.sleep(2)
        papago_translated = papago.find_element(By.ID, 'targetEditArea')
        result = papago_translated.text
    except NoSuchElementException: # 예외처리 (요소를 찾지 못하는 경우)
        result = '번역 오류ㅠㅠ'
    finally:
        papago.close()
    return result
    
    import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import openai


# OPENAI API키 설정
openai.api_key = "OpenAI API Key 입력"

# 크롬드라이버 셋팅
def set_chrome_driver(headless=True):
    options = webdriver.ChromeOptions()
    if headless:
        options.add_argument('headless')
    options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36")
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    return driver

# 뉴스 페이지 크롤링
def crawl_page(url):
    try:
        driver = set_chrome_driver(False)
        driver.get(url)
        # 요소 변경 가능
        article_page = driver.find_element(By.CLASS_NAME, 'articlePage')
        text = article_page.text
        driver.close()
    except NoSuchElementException:
        text = ""
    return text

# ChatGPT 요약
def summarize(text):
    # 모델 엔진 선택
    model_engine = "text-davinci-003"

    # 맥스 토큰
    max_tokens = 2500
    
    # 프롬프트 (요약해줘!)
    prompt = f'''Summarize the paragraph below and interpret whether it is a positive or negative sentiment.

    {text}
    '''

    # 요약 요청
    completion = openai.Completion.create(
        engine=model_engine,
        prompt=prompt,
        max_tokens=max_tokens,
        temperature=0.3,      # creativity
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    return completion.choices[0].text

# 파파고 번역
def papago_translate(text):
    try:
        papago = set_chrome_driver(False)
        papago.get('https://papago.naver.com/')
        time.sleep(1)
        papago.find_element(By.ID, 'txtSource').send_keys(text)
        papago.find_element(By.ID, 'btnTranslate').click()
        time.sleep(2)
        papago_translated = papago.find_element(By.ID, 'targetEditArea')
        result = papago_translated.text
    except NoSuchElementException: # 예외처리 (요소를 찾지 못하는 경우)
        result = '번역 오류ㅠㅠ'
    finally:
        papago.close()
    return result
    
# 5개의 신문기사 URL 만 추출 합니다.
    top5_links = []

for link in top5.find_element(By.CLASS_NAME, 'largeTitle').find_elements(By.CLASS_NAME, 'js-article-item')[:5]:
    top5_links.append(link.find_element(By.CSS_SELECTOR, 'a').get_attribute('href'))
    
    top5_links

# 최종 wrapper
def summarize_news(url):
    page = crawl_page(url)
    ummarized = summarize(page)
    print('[원문 요약]')
    print(summarized)
    korean_translated = papago_translate(summarized)
    print('\n[한글 요약]')
    print(korean_translated)
    return korean_translated
    
    _ = summarize_news('https://www.investing.com/analysis/traders-send-wheat-prices-spiking-as-allied-tanks-aid-to-roll-into-ukraine-200634894')
    
 # most popular news 의 신문기사 요소를 크롤링 합니다
    top5 = set_chrome_driver(False)
 # URL 요청
    top5.get('https://www.investing.com/news/most-popular-news')
 # 5개의 요소만 가져옵니다.
    top5.find_element(By.CLASS_NAME, 'largeTitle').find_elements(By.CLASS_NAME, 'js-article-item')[:5]
 
 # 5개의 신문기사 URL 만 추출 합니다.
    top5_links = []

 for link in top5.find_element(By.CLASS_NAME, 'largeTitle').find_elements(By.CLASS_NAME, 'js-article-item')[:5]:
    top5_links.append(link.find_element(By.CSS_SELECTOR, 'a').get_attribute('href'))
    
    top5_links
 
 # 5개의 신문기사 링크에 대한 본문 크롤링+요약+번역 을 진행합니다.
    top5_summarize = []

 for link in top5_links:
    output = summarize_news(link)
    top5_summarize.append(output)
    print()
 
