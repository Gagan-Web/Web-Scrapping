from bs4 import BeautifulSoup
import requests
import pandas as pd
from dotenv import load_dotenv
import os

load_dotenv()
agent = os.getenv("USER_AGENT")
print(agent)

url = "https://www.amazon.com/s?k=gaming&crid=2WQBWMQC7GGTV&sprefix=gaming%2Caps%2C264&ref=nb_sb_noss_1"
Headers = ({'User-Agent': agent, 'Accept-Language': 'en-US, en;q=0.9'})


# ----------------------------------------------------------------------------------------
webpage = requests.get(url, headers=Headers)
# print(webpage.status_code)
soup = BeautifulSoup(webpage.content, "html.parser")
links = soup.find_all("a", attrs = {"class": "a-link-normal s-line-clamp-3 s-link-style a-text-normal"})
link = links[0].get("href")
product_list = "https://www.amazon.com" + link


# -----------------------------------------------------------------------------------------
new_webpage = requests.get(product_list, headers=Headers)
print(new_webpage.status_code)

# print(new_webpage.status_code)
new_soup = BeautifulSoup(new_webpage.content, "html.parser")

print("New_soup title:", new_soup.title)

product_title = new_soup.find("span", attrs = {"id": "productTitle"}).text.strip()
print(product_title)

price_tag = new_soup.find("span", class_="a-offscreen")
if price_tag:
    product_price = price_tag.get_text(strip=True)
    print(product_price.replace("INR","INR "))
else:
    print("Price not found")

product_rating = new_soup.find("span", attrs = {"class": "a-icon-alt"}).text.strip()
print(product_rating)