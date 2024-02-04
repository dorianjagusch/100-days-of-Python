from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import requests
from time import sleep
import re

FORM_LINK = "https://docs.google.com/forms/d/e/1FAIpQLSc4Vav_UHGSdG76JZBodxthpICgPm-4B51syhRGLUoTj_XxiQ/viewform?usp=sf_link"
ZILLOW_LINK = "https://appbrewery.github.io/Zillow-Clone/"


def scrape_zillow():
    response = requests.get(ZILLOW_LINK)
    response.raise_for_status()
    soup = BeautifulSoup(response.text, "html.parser")
    addresses_raw = soup.find_all(name="address", attrs={"data-test": "property-card-addr"})
    links_raw = soup.select('.StyledPropertyCardDataWrapper a[data-test="property-card-link"]')
    print(len(links_raw))
    prices_raw = soup.find_all(name="span", attrs={"data-test": "property-card-price"})


    addresses = [",".join(address.getText().strip().replace("|", ",").split(",")[1:]).strip() for address in addresses_raw]
    links = [link["href"] for link in links_raw]
    prices = [re.split("\+|/", price.getText())[0] for price in prices_raw]

    return addresses, prices, links

"""
    addresses = 'address data-test="property-card-addr"'
    links = 'address data-test="property-card-link"'
    prices = 'span data-test="property-card-price"'
"""


def fill_form(findings):
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_experimental_option("detach", True)
    driver = webdriver.Chrome(chrome_options)

    driver.get(FORM_LINK)
    sleep(1)

    for (address, price, link) in zip(*findings):
        input_fields = driver.find_elements(By.CSS_SELECTOR, "input[type='text']")
        input_fields[0].send_keys(address)
        input_fields[1].send_keys(price)
        input_fields[2].send_keys(link)
        send_button = driver.find_element(By.CSS_SELECTOR, 'div[role="button"]')
        send_button.click()
        sleep(1)

        repeat_link = driver.find_element(By.LINK_TEXT, "Lähetä toinen vastaus")
        repeat_link.click()
        sleep(1)

    driver.quit()


if __name__ == "__main__":
    findings = scrape_zillow()
    fill_form(findings)
