import requests
import dotenv, os
from bs4 import BeautifulSoup
import smtplib
import lxml

url = "https://www.amazon.de/-/en/Complete-Ultimate-Tutorial-Microcontroller-Accessories/dp/B01IHCCKKK/ref=sr_1_3?crid=OKD7UKVJBXXN&keywords=arduino+starter+kit&qid=1706984012&sprefix=arduini%2Caps%2C155&sr=8-3"

CUT_OFF = 50.00

USER_AGENT = os.getenv("USER_AGENT")
ACCEPT_LANG = os.getenv("ACCEPT_LANG")
EMAIL_PW = os.getenv("EMAIL_PW")
EMAIL = os.getenv("EMAIL")

headers = {
    "Accept-Language": ACCEPT_LANG,
    "User_Agent": USER_AGENT,
}

response = requests.get(url, headers=headers)
response.raise_for_status()
content = response.text

soup = BeautifulSoup(content, "lxml")

price = int(soup.find(name="span", class_="a-price-whole").getText())

if price < CUT_OFF:
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=EMAIL, password=EMAIL_PW)
        connection.sendmail(from_addr=EMAIL, to_addrs=EMAIL,
                            msg="Low Price!!\n\nYour product is at a low price. Grab it while it's low:\n\n"
                                f"{url}")
