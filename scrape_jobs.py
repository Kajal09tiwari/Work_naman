
##################################################################################################

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from pymongo import MongoClient
import time

client = MongoClient("mongodb+srv://kt3082006:kajal@webscrape.nzhi7b1.mongodb.net/?retryWrites=true&w=majority")
db = client["job_scraper_db"]            
collection = db["naukri_jobs"]           


chrome_options = Options()
chrome_options.add_argument("--start-maximized")
driver = webdriver.Chrome(options=chrome_options)


driver.get("https://www.naukri.com/python-developer-jobs")
time.sleep(5)  

print("📄 Scraping Page 1...\n")
job_cards = driver.find_elements(By.CLASS_NAME, "cust-job-tuple")

print(f"✅ Found {len(job_cards)} job listings.\n")

for index, job in enumerate(job_cards, start=1):
    try:
        title = job.find_element(By.CLASS_NAME, "title").text
    except NoSuchElementException:
        title = "N/A"

    try:
        company = job.find_element(By.CSS_SELECTOR, "a.comp-name").text
    except NoSuchElementException:
        company = "N/A"

    try:
        location = job.find_element(By.CLASS_NAME, "location").text
    except NoSuchElementException:
        location = "N/A"

    try:
        experience = job.find_element(By.CLASS_NAME, "exp").text
    except NoSuchElementException:
        experience = "N/A"

    try:
        salary = job.find_element(By.CLASS_NAME, "salary").text
    except NoSuchElementException:
        salary = "N/A"

    try:
        posted_date = job.find_element(By.CLASS_NAME, "type").text
    except NoSuchElementException:
        posted_date = "N/A"

   
    try:
        jd_url = job.find_element(By.CLASS_NAME, "jd-url").get_attribute("href")  
    except NoSuchElementException:
        jd_url = "N/A"

    try:
        email = job.find_element(By.CLASS_NAME, "email").text  
    except NoSuchElementException:
        email = "N/A"

   
    job_data = {
        "id": index,  
        "designation": title, 
        "location": location,
        "jobinfo": "N/A",  
        "description": "N/A",  
        "min_experience": experience.split("-")[0].strip() if experience != "N/A" else "N/A",  
        "max_experience": experience.split("-")[1].strip() if experience != "N/A" else "N/A",
        "company": company,
        "jd_url": jd_url,
        "vacancies": "N/A",  
        "logo_url": "N/A",  
        "te_logo_url": "N/A", 
        "white_listed_keywords": "N/A",  
        "keywords": "N/A",  
        "keywords_ar": "N/A",  
        "email": email,
        "is_easy_apply": "N/A",  
        "job_id": str(index),  
        "job_posted_date_time": posted_date,
        "min_Salary": salary,  
        "max_Salary": salary,  
        "Country": "India",  
        "State": "N/A",  
        "City": location,
        "functional_Domain": "N/A",  
        "sector_industry_Domain": "N/A",  
        "icon": "N/A",  
        "skills": "N/A",  
        "program_ids": "N/A",  
        "gulf_id": "N/A",  
        "education": "N/A",  
        "nationality": "N/A", 
        "gender": "N/A",  
        "chart_key": "N/A",  
        "job_role": title,  
        "job_designation": title,  
        "status": "Active",  
        "created_at": time.strftime("%Y-%m-%d %H:%M:%S"),  
        "updated_at": time.strftime("%Y-%m-%d %H:%M:%S"),
        "source": "Naukri",
        "organization_id": index  
    }

   
    try:
        collection.insert_one(job_data)
        print(f"✅ Inserted Job {index}: {title}")
    except Exception as e:
        print(f"❌ Error inserting Job {index}: {e}")

driver.quit()
print("\n🎉 All jobs inserted into MongoDB Atlas successfully.")
