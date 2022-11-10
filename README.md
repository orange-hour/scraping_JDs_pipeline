# 데이터 직군의 채용공고 수집, 정제 및 적재를 통한 채용공고 데이터셋 구축


## 프로젝트 목표

각 기업의 데이터 직군 채용공고들을 수집 및 적재하고, 업데이트하는 과정을 자동화하여 채용공고 데이터셋을 구축하고 유지한다.  


## 프로젝트 진행 방식

* 데이터 수집: Selenium을 이용한 동적 웹 스크래핑
+) Scheduling 관련 라이브러리 활용: 일정 주기로 업데이트 → 공고 수정사항 및 새로 올라온 공고 반영  
* 데이터 적재: MySQL 로컬 DB 이용 

## 프로젝트 활용 데이터

**스크래핑을 시도할 웹사이트 목록**

- 자소설닷컴 ([https://jasoseol.com/recruit](https://jasoseol.com/recruit))
- 원티드 ([https://www.wanted.co.kr/](https://www.wanted.co.kr/))
- 링크드인 ([https://www.linkedin.com/feed/](https://www.linkedin.com/feed/))
- 외 각 기업 채용 페이지
    - 카카오 ([https://careers.kakao.com/index](https://careers.kakao.com/index))
    - 네이버 ([https://recruit.navercorp.com/](https://recruit.navercorp.com/))
    - 라인 ([https://careers.linecorp.com/](https://careers.linecorp.com/))
