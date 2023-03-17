# pip install requests
import requests
from pprint import pprint

manzil = 'https://daryo.uz/'
r = requests.get(manzil)
pprint(r.text)
