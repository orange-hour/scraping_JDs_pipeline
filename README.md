# Selenium을 이용한 채용공고 데이터 파이프라인 구축

---

**프로젝트 기간:** 2022.11.03 ~ 14 (12일)

**프로젝트 도구:** Selenium, MySQL, DBeaver, Pandas

**사용 언어:** Python, SQL

---

### 프로젝트 개요

- 채용사이트에서 데이터 직군 채용공고들을 크롤링하여 MySQL DB에 적재하는 과정을 자동화
- MySQL 로컬 데이터베이스에 데이터 적재 - 총 1053개 채용 공고 적재 성공

### 프로젝트 배경

- 본 프로젝트는 코드스테이츠와의 기업협업 프로젝트로 진행됨
- 문제 상황: 코드스테이츠는 AI 부트캠프 수강생들에게 실무 중심의 교육을 제공하기 위해 채용공고 데이터를 기반으로 교육과정을 개선하여야 함
- 해결책: 데이터 직군의 채용공고 수집, 정제 및 적재를 위한 파이프라인을 구축해 코드스테이츠에서 채용공고 데이터를 활용할 수 있도록 함

### 프로젝트 기술 스택

- **Web Scraping**
    
    ![Selenium](https://img.shields.io/badge/Selenium-43B02A?style=for-the-badge&logo=selenium&logoColor=white) ![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white) ![Pandas](https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white) 
   
- **Database**
    
    ![MySQL](https://img.shields.io/badge/mysql-4479A1?style=for-the-badge&logo=mysql&logoColor=white)
    
- **Tools**
    
    ![github](https://img.shields.io/badge/github-181717?style=for-the-badge&logo=github&logoColor=white)
    

**Selenium 선택 이유**

- 원티드를 비롯한 일부 채용 플랫폼은 페이지 내부에서 스크롤을 해야만 모든 채용공고를 열람할 수 있어, 동적 웹 스크래핑이 가능한 Selenium 사용


### 프로젝트 진행 과정

1. 원티드 (https://www.wanted.co.kr/) 스크래핑 진행
2. 원티드에 올라온 채용공고 중 아래 4가지 카테고리에 해당하는 직군의 채용공고만 스크래핑
• 1) 데이터 엔지니어, 2) 빅데이터 엔지니어, 3) DevOps/시스템 관리자, 4) DBA
3. 수집한 공고 데이터를 로컬에 csv 파일로 저장하여 Pandas를 통해 정제 (결측값 표시, 개행문자 제거 등)
4. 로컬에 새로운 MySQL DB 생성 및 csv 파일 bulk upload를 통한 데이터 적재


### 프로젝트 구현 내용

(수정 및 이미지 추가 필요)

*스크래퍼 작동 방식*
1. 원티드에서 특정 카테고리의 채용공고만 선택한 웹사이트 링크로 접속 
2. 해당 페이지 끝까지 스크롤
3. 해당 페이지 내 존재하는 채용공고의 링크 정보 수집 (list로 저장)
4. list에 저장된 링크 각각에 접속하여 아래 정보 스크래핑
• 포지션명, 회사명, 근무지, 직무 소개, 주요 업무, 자격요건, 우대사항, 혜택 및 복지 
5. 링크에 모두 접속하고 나면 스크래핑한 정보를 로컬 저장소에 별도의 csv 파일로 저장



### 프로젝트 한계 및 개선 방안

**한계**

- 원티드 외 다양한 채용공고 웹사이트의 데이터 수집을 진행하지 못함 (타 채용 플랫폼 및 각 기업 채용사이트 등)
- 로컬 데이터베이스를 사용하여 일정 저장공간 초과 시 추가적인 데이터 적재가 어려움
- 배치 스케줄링을 하지 않아 채용 공고 데이터가 자동으로 업데이트되지 않음

**개선 방안**

- 보다 많은 사이트 의 채용공고를 스크래핑할 수 있도록 원티드 외 사이트에 대해서도 추가적으로 스크래핑 구현
- AWS S3 등을 이용한 클라우드 DB 구축
- Airflow를 이용하여 배치 데이터 처리 진행 및 데이터 파이프라인 자동화


