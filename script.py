import requests
import os

r = requests.get("www.google.ca")
print(r.status_code)
