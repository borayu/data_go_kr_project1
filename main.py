import requests
from urllib import parse

base_url = "http://apis.data.go.kr/B090041/openapi/service/SpcdeInfoService/"
api_key = "cTWUGiJR/GRNsWP1Zvpr6EfojgF2NzRo6pzKHUXZplHewa1M8A9dkuiqnqsbVFTvix8hc8GWw4abmLFx7YB5tA=="

url_holiday = base_url + 'getRestDeInfo'

params = {'ServiceKey':api_key,
          'solYear':2022,
          'numOfRows':100
}

response = requests.get(url_holiday, params)
print(response.text)