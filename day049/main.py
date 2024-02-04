from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
import time
import dotenv, os


dotenv.load_dotenv()

EMAIL = os.getenv("EMAIL")
PW = os.getenv("PW")

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(chrome_options)

driver.get("https://www.linkedin.com/jobs/search/?currentJobId=3818181529&f_LF=f_AL&geoId=102257491&keywords=python%20developer&location=London%2C%20England%2C%20United%20Kingdom")

time.sleep(2)

driver.find_element(By.LINK_TEXT, "Sign in").click()

time.sleep(2)

driver.find_element(By.NAME, "session_key").send_keys(EMAIL)
driver.find_element(By.NAME, "session_password").send_keys(PW, Keys.ENTER)

time.sleep(5)

driver.find_element(By.XPATH, "/html/body/div[6]/div[4]/aside[1]/div[1]/header/div[3]/button[2]").click()
time.sleep(4)
job_cards = driver.find_element(by=By.CSS_SELECTOR, value=".scaffold-layout__list-container")\
    .find_elements(By.TAG_NAME, "li")

cards = 0
for job in job_cards:
    if cards == 7:
        cards = 0
        ActionChains(driver).scroll_to_element(job).perform()
        time.sleep(5)
        new_jobs = driver.find_elements(by=By.CSS_SELECTOR, value=".job-card-container--clickable")
        for new_job in new_jobs:
            if new_job not in job_cards:
                job_cards.append(new_job)
    job.click()
    time.sleep(1)
    driver.find_element(By.CSS_SELECTOR, ".jobs-save-button").click()
    follow_button = driver.find_element(By.CSS_SELECTOR, ".follow")
    ActionChains(driver).scroll_to_element(follow_button).perform()
    follow_button.click()
    time.sleep(3)
    cards += 1
driver.quit()






