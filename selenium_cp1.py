import time
from selenium import webdriver
from selenium.webdriver.common.by import By # 언제까지 브라우저 접속 기다려주겠다
from selenium.webdriver.support import expected_conditions as EC # 어떤 상태까지 기다리겠다(페이지 클릭이나 커서 이동)
from selenium.webdriver.chrome.options import Options

driver = webdriver.Chrome(executable_path="/Users/orangehour/Downloads/chromedriver")

# #원티드 채용공고 목록 링크: 직군 중 데이터 엔지니어, 빅데이터 엔지니어, DevOps / 시스템 관리자, DBA 선택
# url_data_engineer = "https://www.wanted.co.kr/wdlist/518?country=kr&job_sort=company.response_rate_order&years=-1&selected=655&selected=1025&selected=674&selected=10231&locations=all"


# driver.get(url_data_engineer)

# SCROLL_PAUSE_SEC = 2  #매 스크롤마다 데이터 로딩시간 고려

# # 스크롤 높이 가져옴
# last_height = driver.execute_script("return document.body.scrollHeight") #페이지 끝까지 스크롤

# while True: #페이지 끝까지 반복
#     # 끝까지 스크롤 다운
#     driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

#     # 1초 대기
#     time.sleep(SCROLL_PAUSE_SEC)

#     # 스크롤 다운 후 스크롤 높이 다시 가져옴
#     new_height = driver.execute_script("return document.body.scrollHeight")
#     if new_height == last_height:
#         break
#     last_height = new_height

#공고별 상세페이지
TITLE_XPATH = "//*[@id='__next']/div[3]/div[1]/div[1]/div[1]/section[2]/h2"
COMPANY_NAME_XPATH = "//*[@id='__next']/div[3]/div[1]/div[1]/div[1]/section[2]/div[1]/h6/a"
LOCATION_CLASS = "JobHeader_mobileLocationContainer__DyxUQ"
LOCATION_XPATH = "//*[@id='__next']/div[3]/div[1]/div[1]/div[1]/section[2]/div[1]/span"

#텍스트 내용
INTRO_XPATH = "//*[@id='__next']/div[3]/div[1]/div[1]/div[1]/div[2]/section/p[1]/span"
MAIN_TASK_XPATH = "//*[@id='__next']/div[3]/div[1]/div[1]/div[1]/div[2]/section/p[2]/span"
REQUIREMENTS_XPATH = "//*[@id='__next']/div[3]/div[1]/div[1]/div[1]/div[2]/section/p[3]/span"
PREFER_XPATH = "//*[@id='__next']/div[3]/div[1]/div[1]/div[1]/div[2]/section/p[4]/span"
BENEFITS_XPATH = "//*[@id='__next']/div[3]/div[1]/div[1]/div[1]/div[2]/section/p[5]/span" 


#각 채용공고 클릭
# postings = driver.find_elements_by_class_name("Card_className__u5rsb")
# print(postings)

two_dim_list = []  #전체 리스트
post_list = []  #각 포스팅 하나당 리스트

#테스트 코드
url_tada_engineer = "https://www.wanted.co.kr/wd/135370"

posting = driver.get(url_tada_engineer)
#회사 정보 크롤링
job_title = driver.find_element_by_xpath(TITLE_XPATH).text  #채용 포지션 이름
company_name = driver.find_element_by_xpath(COMPANY_NAME_XPATH).text  #회사명
location = driver.find_element_by_xpath(LOCATION_XPATH).text  #근무지 (ex: 서울.한국)

#공고 본문 크롤링
intro = driver.find_element_by_xpath(INTRO_XPATH).text
main_task = driver.find_element_by_xpath(MAIN_TASK_XPATH).text  #주요업무
requirements = driver.find_element_by_xpath(REQUIREMENTS_XPATH).text  #자격요건
prefer = driver.find_element_by_xpath(PREFER_XPATH).text  #우대사항
benefits = driver.find_element_by_xpath(BENEFITS_XPATH).text  #혜택 및 복지

#location parsing
city, country = location.split('.')

post_list += [job_title, company_name, city, country, intro, main_task, requirements, prefer, benefits]
two_dim_list.append(post_list)

print(len(post_list)) #9가지 요소 다 scraping되었는지 확인
i = 0
for ele in post_list:
    if ele != "":
        i += 1
print(i)  #리스트 내부에 빈 값이 없는지 확인

print(len(two_dim_list)) #scraping 완료된 전체 채용공고 갯수 확인

# for posting in postings:
#     post_list = []
#     posting.click()
#     job_title = driver.find_elements_by_xpath(TITLE_XPATH).text
#     company_name = driver.find_elements_by_xpath(COMPANY_NAME_XPATH).text
#     city = driver.find_elements_by_xpath(CITY_XPATH).text
#     country = driver.find_elements_by_xpath(COUNTRY_XPATH).text
#     intro = driver.find_elements_by_xpath(INTRO_XPATH).text
#     main_task = driver.find_elements_by_xpath(MAIN_TASK_XPATH).text
#     requirements = driver.find_elements_by_xpath(REQUIREMENTS_XPATH).text
#     prefer = driver.find_elements_by_xpath(PREFER_XPATH).text
#     benefits = driver.find_elements_by_xpath(BENEFITS_XPATH).text
#     post_list += [company_name, city, country, intro, main_task, requirements, prefer]
#     two_dim_list.append(post_list)

    



