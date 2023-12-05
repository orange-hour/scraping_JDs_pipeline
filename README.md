# Generating a Job Description Dataset with Web Scraping


**Project Duration:** 2022.11.03 ~ 11.14 <br>


### Project Overview

- Automated the process of scraping and loading job postings from a job board site into a MySQL DB
- Loaded data into a MySQL database - 1053 total postings successfully loaded

### Background
**Problem Statement:**
CodeStates, in its pursuit of delivering cutting-edge training in artificial intelligence through bootcamps, identified the need to refine its curriculum based on real-world job posting data. The objective was to offer students a more hands-on and industry-aligned learning experience.

**Proposed Solution:**
The development of a pipeline designed to efficiently collect, cleanse, and load job postings specifically related to data positions.

### Used Skills

- **Web Scraping**
    
    ![Selenium](https://img.shields.io/badge/Selenium-43B02A?style=for-the-badge&logo=selenium&logoColor=white) ![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white) ![Pandas](https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white) 
   
- **Database**
    
    ![MySQL](https://img.shields.io/badge/mysql-4479A1?style=for-the-badge&logo=mysql&logoColor=white)

**Reasons for Choosing Selenium**
- Used Selenium as dynamic web scraping is needed to enable scrolling inside the job board platform, Wanted, scraped in this project.

### Project implementation details

1. Uses a web scraper to scrape job posting data from Wanted and save it as a CSV file

> **How the Scraper Works** <br>
> ① Filters jobs on Wanted that have a specific category and scrolls to the end of the page <br>
> ② Scrapes links of each job post on the page and accesses each post to scrape the job description data <br>
> ③ Saves the data to a CSV file

2. Cleans data with Pandas (showing missing values, removing newlines)

3. Loads the data to a local MySQL database


### Project limitations and future improvements

**Limitations**

- Not collecting data from various job posting websites other than Wanted
- Difficulty loading additional data when the database exceeds a certain amount of storage space due to using a local MySQL database
- No batch scheduling to automatically update job posting data

**Improvements**

- Developing additional web scraping processes for platforms other than Wanted
- Implementing a cloud data warehouse using Google Bigquery
- Batch data processing and data pipeline automation using Airflow


