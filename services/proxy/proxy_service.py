import random
import requests

def get_proxy() -> str:
  api_url = "https://raw.githubusercontent.com/TheSpeedX/SOCKS-List/master/http.txt"
  response = requests.get(api_url)
  response.raise_for_status()
  proxies = response.text.strip().splitlines()
  return random.choice(proxies)
