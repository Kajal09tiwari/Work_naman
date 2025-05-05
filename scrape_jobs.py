# # from selenium import webdriver
# # from selenium.webdriver.chrome.service import Service
# # from selenium.webdriver.chrome.options import Options
# # from selenium.webdriver.common.by import By  # ❗️You missed this import
# # from webdriver_manager.chrome import ChromeDriverManager
# # import time  # ❗️You also forgot to import time module
# # from selenium.webdriver.support.ui import WebDriverWait
# # from selenium.webdriver.support import expected_conditions as EC
# # options = Options()
# # # options.add_argument("--headless")
# # options.add_argument("--window-size=1920,1080")
# # # Automatically download and use the correct ChromeDriver
# # driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
# # # Define job sites and their specific rules
# # job_sites = {
# #     # "Indeed": {
# #     #     "url": "https://www.indeed.com/jobs?q=Python+Developer&l=Remote",
# #     #     "job_card": "tapItem",
# #     #     "title": (By.CLASS_NAME, "jobTitle"),
# #     #     "company": (By.CLASS_NAME, "companyName"),
# #     #     "location": (By.CLASS_NAME, "companyLocation"),
# #     # },
# #     "Naukri": {
# #     "url": "https://www.naukri.com/python-developer-jobs",
# #     "job_card": "srp-jobtuple-wrapper",  # ✅ Correct class from screenshot
# #     "title": (By.CLASS_NAME, "title"),
# #     "company": (By.CLASS_NAME, "subTitle"),
# #     "location": (By.CLASS_NAME, "location"),
# # },
# #     # You can add more job portals here with their DOM structure
# # }
# # def scrape_jobs(site_name, config):
# #     print(f"\n🔍 Scraping {site_name}...")
# #     driver.get(config["url"])
# #     WebDriverWait(driver, 30).until(
# #     EC.presence_of_all_elements_located((By.CLASS_NAME, config["job_card"]))
# # )
# # #Wait for JavaScript content to load
# #     job_cards = driver.find_elements(By.CLASS_NAME, config["job_card"])
# #     print(f"✅ Found {len(job_cards)} job listings.\n")
# #     for job in job_cards:
# #         try:
# #             title = job.find_element(*config["title"]).text
# #             company = job.find_element(*config["company"]).text
# #             location = job.find_element(*config["location"]).text
# #             print(f"📌 Title: {title}\n🏢 Company: {company}\n📍 Location: {location}\n")
# #         except Exception:
# #             continue
# # # Run scraper for each site
# # for site, config in job_sites.items():
# #     scrape_jobs(site, config)
# # driver.quit()
# # # from selenium import webdriver
# # # from selenium.webdriver.chrome.service import Service
# # # from webdriver_manager.chrome import ChromeDriverManager
# # # driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
# # # driver.get("https://www.google.com")
# # # print(driver.title)
# # # driver.quit()






# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.chrome.options import Options
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from webdriver_manager.chrome import ChromeDriverManager
# import time

# options = Options()
# options.add_argument("--start-maximized")

# driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

# def scrape_naukri_jobs():
#     base_url = "https://www.naukri.com/python-developer-jobs"
#     driver.get(base_url)

#     page = 1
#     while True:
#         print(f"\n📄 Scraping Page {page}...\n")

#         try:
#             WebDriverWait(driver, 20).until(
#                 EC.presence_of_all_elements_located((By.CLASS_NAME, "srp-jobtuple-wrapper"))
#             )
#             time.sleep(2)

#             job_cards = driver.find_elements(By.CLASS_NAME, "srp-jobtuple-wrapper")
#             print(f"✅ Found {len(job_cards)} job listings on page {page}.\n")

#             for job in job_cards:
#                 try:
#                     title = job.find_element(By.CLASS_NAME, "title").text
#                     company = job.find_element(By.CLASS_NAME, "subTitle").text
#                     location = job.find_element(By.CLASS_NAME, "location").text
#                     print(f"📌 Title: {title}\n🏢 Company: {company}\n📍 Location: {location}\n")
#                 except:
#                     continue

#             # Check if "Next" button is enabled
#             try:
#                 pagination = WebDriverWait(driver, 10).until(
#                     EC.presence_of_element_located((By.CSS_SELECTOR, "div.styles_pagination__olvXh"))
#                 )
#                 next_button = driver.find_element(By.XPATH, "//a[contains(text(), 'Next')]")


#                 # If the "Next" button is disabled, stop
#                 if 'disabled' in next_button.get_attribute('class') or not next_button.is_enabled():
#                     print("🚫 'Next' button disabled. Stopping.")
#                     break

#                 next_button.click()
#                 page += 1
#                 time.sleep(3)
#             except Exception as e:
#                 print("🚫 'Next' button not found or not clickable. Exiting.")
#                 break

#         except Exception as e:
#             print(f"❌ Error on page {page}: {e}")
#             break

#     driver.quit()

# scrape_naukri_jobs()

##############################chal rha h###############################

# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.common.by import By
# from selenium.webdriver.chrome.options import Options
# from selenium.common.exceptions import NoSuchElementException
# import time

# # Setup Chrome options
# chrome_options = Options()
# chrome_options.add_argument("--start-maximized")

# # Start the driver
# driver = webdriver.Chrome(options=chrome_options)
# driver.get("https://www.naukri.com/python-developer-jobs")

# print("📄 Scraping Page 1...\n")
# time.sleep(5)  # wait for the page to load

# # Get all job cards
# job_cards = driver.find_elements(By.CLASS_NAME, "cust-job-tuple")

# print(f"✅ Found {len(job_cards)} job listings on page 1.\n")

# for index, job in enumerate(job_cards, start=1):
#     try:
#         title = job.find_element(By.CLASS_NAME, "title").text
#     except NoSuchElementException:
#         title = "Title not found"

#     try:
#         company = job.find_element(By.CSS_SELECTOR, "a.comp-name").text
#     except NoSuchElementException:
#         company = "Company not found"

#     try:
#         location = job.find_element(By.CLASS_NAME, "location").text
#     except NoSuchElementException:
#         location = "Location not found"

#     try:
#         experience = job.find_element(By.CLASS_NAME, "exp").text
#     except NoSuchElementException:
#         experience = "Experience not found"

#     try:
#         salary = job.find_element(By.CLASS_NAME, "salary").text
#     except NoSuchElementException:
#         salary = "Salary not found"

#     try:
#         posted_date = job.find_element(By.CLASS_NAME, "type").text
#     except NoSuchElementException:
#         posted_date = "Date not found"

#     print("══════════════════════════════════════════════════════════════")
#     print(f"🖥️ Job {index}")
#     print(f"📌 Title     : {title}")
#     print(f"🏢 Company   : {company}")
#     print(f"📍 Location  : {location}")
#     print(f"🕒 Experience: {experience}")
#     print(f"💰 Salary    : {salary}")
#     print(f"📅 Posted    : {posted_date}")
#     print("══════════════════════════════════════════════════════════════\n")

# # Done
# driver.quit()
#############################################################################




# from selenium import webdriver
# from selenium.webdriver.chrome.options import Options
# from selenium.webdriver.common.by import By
# from selenium.common.exceptions import NoSuchElementException
# from pymongo import MongoClient
# import time

# # 1. MongoDB Connection Setup
# client = MongoClient("mongodb://localhost:27017/")
# db = client["job_scraper_db"]
# collection = db["naukri_jobs"]

# # 2. Chrome Setup
# chrome_options = Options()
# chrome_options.add_argument("--start-maximized")
# driver = webdriver.Chrome(options=chrome_options)
# driver.get("https://www.naukri.com/python-developer-jobs")
# time.sleep(5)

# print("📄 Scraping Page 1...\n")
# job_cards = driver.find_elements(By.CLASS_NAME, "cust-job-tuple")

# print(f"✅ Found {len(job_cards)} job listings.\n")

# for index, job in enumerate(job_cards, start=1):
#     try:
#         title = job.find_element(By.CLASS_NAME, "title").text
#     except NoSuchElementException:
#         title = "N/A"

#     try:
#         company = job.find_element(By.CSS_SELECTOR, "a.comp-name").text
#     except NoSuchElementException:
#         company = "N/A"

#     try:
#         location = job.find_element(By.CLASS_NAME, "location").text
#     except NoSuchElementException:
#         location = "N/A"

#     try:
#         experience = job.find_element(By.CLASS_NAME, "exp").text
#     except NoSuchElementException:
#         experience = "N/A"

#     try:
#         salary = job.find_element(By.CLASS_NAME, "salary").text
#     except NoSuchElementException:
#         salary = "N/A"

#     try:
#         posted_date = job.find_element(By.CLASS_NAME, "type").text
#     except NoSuchElementException:
#         posted_date = "N/A"

#     # 3. Create dictionary for MongoDB
#     job_data = {
#         "title": title,
#         "company": company,
#         "location": location,
#         "experience": experience,
#         "salary": salary,
#         "posted_date": posted_date
#     }

#     # 4. Insert into MongoDB
#     collection.insert_one(job_data)

#     print(f"✅ Inserted Job {index}: {title}")

# # Done
# driver.quit()
# print("\n🎉 All jobs inserted into MongoDB successfully.")
##################################################################################################

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from pymongo import MongoClient
import time

# MongoDB connection
client = MongoClient("mongodb+srv://kt3082006:kajal@webscrape.nzhi7b1.mongodb.net/?retryWrites=true&w=majority")
db = client["job_scraper_db"]            # Database name
collection = db["naukri_jobs"]           # Collection name

# Selenium WebDriver Setup
chrome_options = Options()
chrome_options.add_argument("--start-maximized")
driver = webdriver.Chrome(options=chrome_options)

# Open the job listing page
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

    # Add more fields to match the job schema
    try:
        jd_url = job.find_element(By.CLASS_NAME, "jd-url").get_attribute("href")  # Assuming job description URL
    except NoSuchElementException:
        jd_url = "N/A"

    try:
        email = job.find_element(By.CLASS_NAME, "email").text  # If available, extract email
    except NoSuchElementException:
        email = "N/A"

    # Map scraped data to the schema
    job_data = {
        "id": index,  # Unique id for the job
        "designation": title,  # Designation or job title
        "location": location,
        "jobinfo": "N/A",  # You can add more details from the job description if needed
        "description": "N/A",  # Job description if it's available
        "min_experience": experience.split("-")[0].strip() if experience != "N/A" else "N/A",  # Example: "2-5 years"
        "max_experience": experience.split("-")[1].strip() if experience != "N/A" else "N/A",
        "company": company,
        "jd_url": jd_url,
        "vacancies": "N/A",  # If available, you can scrape number of vacancies
        "logo_url": "N/A",  # If available, you can scrape company logo
        "te_logo_url": "N/A",  # If available, scrape tech logo URL
        "white_listed_keywords": "N/A",  # If any
        "keywords": "N/A",  # Add keywords here if available
        "keywords_ar": "N/A",  # Arabic keywords if available
        "email": email,
        "is_easy_apply": "N/A",  # If it's easy apply
        "job_id": str(index),  # Job id
        "job_posted_date_time": posted_date,
        "min_Salary": salary,  # Salary range if available
        "max_Salary": salary,  # If salary is given as a range, you can split it
        "Country": "India",  # You can derive from location
        "State": "N/A",  # Derive from location if possible
        "City": location,
        "functional_Domain": "N/A",  # If available
        "sector_industry_Domain": "N/A",  # If available
        "icon": "N/A",  # If available
        "skills": "N/A",  # If skills are listed
        "program_ids": "N/A",  # If available
        "gulf_id": "N/A",  # If available
        "education": "N/A",  # If available
        "nationality": "N/A",  # If nationality is mentioned
        "gender": "N/A",  # Gender preference
        "chart_key": "N/A",  # If available
        "job_role": title,  # Job role
        "job_designation": title,  # Job designation
        "status": "Active",  # Default status
        "created_at": time.strftime("%Y-%m-%d %H:%M:%S"),  # Date of scraping
        "updated_at": time.strftime("%Y-%m-%d %H:%M:%S"),
        "source": "Naukri",
        "organization_id": index  # Unique ID for each job
    }

    # Insert data into MongoDB
    try:
        collection.insert_one(job_data)
        print(f"✅ Inserted Job {index}: {title}")
    except Exception as e:
        print(f"❌ Error inserting Job {index}: {e}")

driver.quit()
print("\n🎉 All jobs inserted into MongoDB Atlas successfully.")
