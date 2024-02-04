from selenium import webdriver
from selenium.webdriver.common.by import By
import time

CHECK_S = 5

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)

driver.get("http://orteil.dashnet.org/experiments/cookie/")
cookie = driver.find_element(By.ID, "cookie")

menu_items = driver.find_elements(By.CSS_SELECTOR, '#store div[class=""]')
prices_raw = driver.find_elements(By.CSS_SELECTOR, "#store div b")

for item in menu_items:
    print(item.text)

prices = [int(price.text.split()[-1].replace(",", "")) for price in prices_raw[:-1]]

print(len(menu_items))

min_5 = time.time() + 5*60
check_time = time.time() + 5

while True:
    cookie.click()
    if time.time() >= check_time:
        money = int(driver.find_element(By.ID, "money").text.replace(",", ""))
        menu_items = driver.find_elements(By.CSS_SELECTOR, '#store div[class=""]')
        menu_items[-1].click()
        check_time = time.time() + 5
        if time.time() >= min_5:
            break


