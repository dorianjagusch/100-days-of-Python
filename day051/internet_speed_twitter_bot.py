from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import ElementClickInterceptedException
import dotenv, os
from time import sleep


dotenv.load_dotenv()

EMAIL = os.getenv("EMAIL")
PASSWORD = os.getenv("PW")
PROMISED_UP = 50
PROMISED_DOWN = 10


class InternetSpeedTwitterBot:

    def __init__(self):
        self.chrome_options = webdriver.ChromeOptions()
        self.chrome_options.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(self.chrome_options)
        self.up = 10
        self.down = 50

    def tweet_at_provider(self):
        self.driver.get("https://twitter.com/?lang=en")

        refuse_cookies = self.driver.find_element(By.XPATH,
                                                  "/html/body/div/div/div/div[1]/div/div/div/div/div/div[2]/div[2]/div/span/span")
        sleep(4)
        refuse_cookies.click()

        login = self.driver.find_element(By.LINK_TEXT, "Sign in")
        login.click()
        sleep(4)
        sign_in_box = self.driver.find_element(By.NAME, "text")
        sign_in_box.send_keys(EMAIL, Keys.ENTER)
        sleep(2)
        input("In case there is a captcha fill it out then press enter, otherwise just enter")
        pw_box = self.driver.find_element(By.NAME, "password")
        pw_box.send_keys(PASSWORD, Keys.ENTER)
        sleep(4)
        tweet = f"Hey Internet Provider, why is my internet speed {self.down}down/{self.up}up when I pay for {PROMISED_DOWN}down/{PROMISED_UP}"

        tweet_field = self.driver.find_element(By.CSS_SELECTOR, 'div[role="textbox"]')
        tweet_field.send_keys(tweet)
        sleep(10)

        post = self.driver.find_element(By.CSS_SELECTOR, 'div[data-testid="tweetButtonInline"]')
        post.click()

    def get_internet_speed(self):
        self.driver.get("https://www.speedtest.net/")
        sleep(2)
        reject_cookies = self.driver.find_element(By.ID, "onetrust-reject-all-handler")
        reject_cookies.click()
        start_button = self.driver.find_element(By.CLASS_NAME, "js-start-test")
        start_button.click()
        sleep(60)
        try:
            self.down = float(self.driver.find_element(By.CLASS_NAME, "download-speed").text)
            self.up = float(self.driver.find_element(By.CLASS_NAME, "upload-speed").text)
        except ElementClickInterceptedException:
            self.driver.find_element(By.CLASS_NAME, "close-btn").click()
            self.down = float(self.driver.find_element(By.CLASS_NAME, "download-speed").text)
            self.up = float(self.driver.find_element(By.CLASS_NAME, "upload-speed").text)
