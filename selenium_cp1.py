import time
from selenium import webdriver
from selenium.webdriver.common.by import By # 브라우저 접속 기다리기
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC # 어떤 상태까지 기다리겠다(페이지 클릭이나 커서 이동)
from collections import defaultdict


driver = webdriver.Chrome(executable_path="/Users/orangehour/Downloads/chromedriver")

#원티드 채용공고 목록 링크: 직군 중 데이터 엔지니어, 빅데이터 엔지니어, DevOps / 시스템 관리자, DBA 선택
url_data_engineer = "https://www.wanted.co.kr/wdlist/518?country=kr&job_sort=company.response_rate_order&years=-1&selected=655&selected=1025&selected=674&selected=10231&locations=all"
driver.get(url_data_engineer)

# 무한 스크롤 (페이지 끝날 때까지)
SCROLL_PAUSE_SEC = 2  #매 스크롤마다 데이터 로딩시간 고려

# 스크롤 높이 가져옴
last_height = driver.execute_script("return document.body.scrollHeight") #페이지 끝까지 스크롤

while True: #페이지 끝까지 반복
    # 끝까지 스크롤 다운
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    # 설정 시간만큼 대기
    time.sleep(SCROLL_PAUSE_SEC)

    # 스크롤 다운 후 스크롤 높이 다시 가져옴
    new_height = driver.execute_script("return document.body.scrollHeight")
    if new_height == last_height:
        break
    last_height = new_height


#공고별 상세페이지
base_path = "//*[@id='__next']/div[3]/div[1]/div[1]/div[1]/section[2]"

TITLE_XPATH = base_path + "/h2"
TITLE_CLASS = "JobHeader_className__HttDA"

COMPANY_NAME_XPATH = base_path + "/div[1]/h6/a"
LOCATION_CLASS = "JobHeader_mobileLocationContainer__DyxUQ"
LOCATION_XPATH = base_path + "/div[1]/span"

#텍스트 내용
INTRO_XPATH = "//*[@id='__next']/div[3]/div[1]/div[1]/div[1]/div[2]/section/p[1]/span"
MAIN_TASK_XPATH = "//*[@id='__next']/div[3]/div[1]/div[1]/div[1]/div[2]/section/p[2]/span"
REQUIREMENTS_XPATH = "//*[@id='__next']/div[3]/div[1]/div[1]/div[1]/div[2]/section/p[3]/span"
PREFER_XPATH = "//*[@id='__next']/div[3]/div[1]/div[1]/div[1]/div[2]/section/p[4]/span"
BENEFITS_XPATH = "//*[@id='__next']/div[3]/div[1]/div[1]/div[1]/div[2]/section/p[5]/span" 


#각 채용공고 주소 수집
wait = WebDriverWait(driver, 10)
elements = wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME, 'Card_className__u5rsb')))
postings = driver.find_elements_by_css_selector("[aria-label='position link']")
links = [post.get_attribute('href') for post in postings]

# postings = driver.find_elements_by_class_name("Card_className__u5rsb")

# 테스트용 - 처음 100개만 가져오기
# links = links[:200]

two_dim_list = []  #전체 리스트
error_dict = defaultdict(list)  #에러 나는 링크 수집


def scrape_text(selector, method, link):
    #selector = xpath or class name
    #method = 'class_name' / 'xpath'
    #link = page link

    # if selector == TITLE_CLASS:
    #     try:
    #         result_text = driver.find_element_by_class_name(selector).text
    #         return result_text
    #     except:
    #         error_dict[selector].append(link)

    # elif method == 'class_name':
    #     try:
    #         result_text = driver.find_element_by_class_name(selector).get_attribute('innerText')
    #         return result_text
    #     except:
    #         error_dict[selector].append(link)

    if method == 'xpath':
        try:
            result_text = driver.find_element_by_xpath(selector).text
            return result_text
        except:
            error_dict[selector].append(link)

    else:
        return "method error"


for link in links:
    driver.get(link)  #해당 페이지로 이동
    post_list = []  #각 포스팅 하나당 리스트 하나 생성

    #회사 정보 크롤링
    job_title = scrape_text(TITLE_XPATH, 'xpath', link)
    company_name = scrape_text(COMPANY_NAME_XPATH, 'xpath', link)
    location = scrape_text(LOCATION_XPATH, 'xpath', link)

    # company_name = driver.find_element_by_xpath(COMPANY_NAME_XPATH).text  #회사명
    # location = driver.find_element_by_xpath(LOCATION_XPATH).text  #근무지 (ex: 서울.한국)

    #공고 본문 크롤링
    intro = scrape_text(INTRO_XPATH, 'xpath', link)
    main_task = scrape_text(MAIN_TASK_XPATH, 'xpath', link)
    requirements = scrape_text(REQUIREMENTS_XPATH, 'xpath', link)
    prefer = scrape_text(PREFER_XPATH, 'xpath', link)
    benefits = scrape_text(BENEFITS_XPATH, 'xpath', link)

    # intro = driver.find_element_by_xpath(INTRO_XPATH).text
    # main_task = driver.find_element_by_xpath(MAIN_TASK_XPATH).text  #주요업무
    # requirements = driver.find_element_by_xpath(REQUIREMENTS_XPATH).text  #자격요건
    # prefer = driver.find_element_by_xpath(PREFER_XPATH).text  #우대사항
    # benefits = driver.find_element_by_xpath(BENEFITS_XPATH).text  #혜택 및 복지

    #location parsing
    # city, country = location.split('.')

    post_list += [job_title, company_name, location, intro, main_task, requirements, prefer, benefits]
    two_dim_list.append(post_list)


print(len(two_dim_list)) #scraping 완료된 전체 채용공고 갯수 확인

import csv

# two_dim_list를 CSV 파일로 저장하기

file_columns = ['포지션명', '회사명', '근무지', '직무 소개', 
'주요 업무', '자격요건', '우대사항', '혜택 및 복지']

try:
    with open("out.csv", "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(file_columns)
        writer.writerows(two_dim_list)
except IOError:
    print("I/O error")


# # error_dict를 CSV 파일로 저장하기
# csv_columns = ['selector(path)','link']
# # error_dict_list = list(error_dict)

# csv_file = "errors_test.csv"
# try:
#     with open(csv_file, 'w') as csvfile:
#         writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
#         writer.writeheader()
#         for data in error_dict:
#             writer.writerow(data)
# except IOError:
#     print("I/O error")


    



