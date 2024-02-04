from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
from selenium.common.exceptions import ElementClickInterceptedException
import dotenv
import os
from time import sleep

dotenv.load_dotenv()

INSTA_USERNAME = os.getenv("INSTA_USERNAME")
INSTA_PW= os.getenv("INSTA_PW")
TARGET_ACCOUNT = os.getenv("TARGET_ACCOUNT")


class InstaFollowBot:

    def __init__(self):
        self.chrome_options = webdriver.ChromeOptions()
        self.chrome_options.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(self.chrome_options)

    def login(self):
        self.driver.get("https://www.instagram.com/")
        sleep(5)

        cookie_decline = self.driver.find_element(By.XPATH, "/html/body/div[4]/div[1]/div/div[2]/div/div/div/div/div[2]/div/button[2]")
        cookie_decline.click()
        sleep(2)

        username_field = self.driver.find_element(By.NAME, "username")
        username_field.send_keys(INSTA_USERNAME)
        pw_field = self.driver.find_element(By.NAME, "password")
        pw_field.send_keys(INSTA_PW)
        sleep(1)
        login_button = self.driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]')
        login_button.click()
        sleep(10)

        no_save_login = self.driver.find_element(By.XPATH, '//div[contains(text(), "Not now")]')
        no_save_login.click()
        sleep(5)

        no_notification = self.driver.find_element(By.XPATH, '//button[contains(text(), "Not Now")]')
        no_notification.click()
        sleep(5)

    def find_followers(self):
        sleep(5)
        # Show followers of the selected account. 
        self.driver.get(f"https://www.instagram.com/{TARGET_ACCOUNT}/followers")

        sleep(5.2)
        # The xpath of the modal that shows the followers will change over time. Update yours accordingly.
        modal_xpath = "/html/body/div[6]/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[2]"
        modal = self.driver.find_element(by=By.XPATH, value=modal_xpath)
        for i in range(5):
            self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", modal)
            sleep(2)

    def follow(self):
        all_follow_buttons = self.driver.find_elements(By.CSS_SELECTOR, "._aano button")
        print(len(all_follow_buttons))
        for button in all_follow_buttons:
            try:
                ActionChains(self.driver).scroll_to_element(button).perform()
                button.click()
                sleep(1.1)
            except ElementClickInterceptedException:
                cancel_button = self.driver.find_element(by=By.XPATH, value="//button[contains(text(), 'Cancel')]")
                cancel_button.click()
                button.click()
