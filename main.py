import requests
from urllib import parse

base_url = "http://apis.data.go.kr/B090041/openapi/service/SpcdeInfoService/"
api_key = "RzW8ODz9lh8si4bAVAPZHzhdc1YUo3+vqN4bEJu3OWGrHovkDHvo46nx72i7NGK5STsjJgw4H19FhJbJY1zWtw=="

url_holiday = base_url + 'getRestDeInfo'

params = {'ServiceKey':api_key,
          'solYear':2022,
          'numOfRows':100
}

response = requests.get(url_holiday, params)
print(response.text)

