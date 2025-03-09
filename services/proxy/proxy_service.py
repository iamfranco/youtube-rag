import random
import requests

def get_proxy() -> dict:
  api_url = "https://raw.githubusercontent.com/TheSpeedX/SOCKS-List/master/http.txt"
  response = requests.get(api_url)
  response.raise_for_status()
  proxies = response.text.strip().splitlines()
  proxy = random.choice(proxies)
  return {"http": f"http://{proxy}"}
