## Import libraries
import requests
import pandas as pd
import csv
import os
from dotenv import load_dotenv
from bs4 import BeautifulSoup
from urllib.parse import urlencode

# URL Structure for Listing VS Review Page:
# Listing: https://www.amazon.com/New-Apple-AirPods-Max-Green/dp/B08PZD76NP/ref=cm_cr_arp_d_product_top?ie=UTF8&th=1
# Reviews: https://www.amazon.com/Headphones-Cancelling-Transparency-Bluetooth-Headphones/product-reviews/B08PZD76NP/ref=cm_cr_othr_d_show_all_btm?ie=UTF8&reviewerType=all_reviews
# Positive: https://www.amazon.com/Headphones-Cancelling-Transparency-Bluetooth-Headphones/product-reviews/B08PZD76NP/ref=cm_cr_arp_d_viewopt_sr?ie=UTF8&reviewerType=all_reviews&filterByStar=positive&pageNumber=1
# Critical: https://www.amazon.com/Headphones-Cancelling-Transparency-Bluetooth-Headphones/product-reviews/B08PZD76NP/ref=cm_cr_arp_d_viewopt_sr?ie=UTF8&reviewerType=all_reviews&filterByStar=critical&pageNumber=1

load_dotenv()
api_key = os.environ.get("api_key")
url = 'https://www.amazon.com/New-Apple-AirPods-Max-Green/dp/B08PZD76NP/ref=cm_cr_arp_d_product_top?ie=UTF8&th=1'
params = {'api-key':api_key, 'url':url}
# print(api_key)

# response = requests.get('http://api.scraperapi.com/', params=urlencode(params))
# soup = BeautifulSoup(response.text, 'html.parser')
# print(soup)

# headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.71 Safari/537.36'}
# website = requests.get(URL, headers=headers)
# results = BeautifulSoup(website.content, 'html.parser')
# print(results)