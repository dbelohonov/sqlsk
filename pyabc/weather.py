# Weather Application

from pyabc.config import *

import urllib.request
import urllib.parse
import json
import sys

print("Weather API Test")
url = 'https://api.weatherapi.com/v1/current.json?key=' + api_key + '&q=London&aqi=no'
url
response = urllib.request.urlopen(url)
print(response.code)
html = response.read()
html
html = html.decode('utf-8')
print(html)



# Использование переменных для конструирования строки GET запроса с параметрами

api_host = "https://api.weatherapi.com"
api_version = "v1"
api_req_typ = 'current.json'
# Token – служит для идентификации

api_city = 'Bratislava'

query_args = {'key': api_key, 'q': api_city, 'aqi': 'no'}
print(query_args)
query_args_str = urllib.parse.urlencode(query_args)
query_args_str
service_uri = api_host + '/' + api_version + '/' + api_req_typ + '?' + query_args_str
service_uri


# Так готовится GET запрос
request = urllib.request.Request(service_uri)

response = urllib.request.urlopen(request)
response.code
response
data_out = response.read()
data_out
data_out.decode('utf-8')

result = json.loads(data_out.decode('utf-8'))
result
result['location']['name']
result['location']['country']
result['current']['temp_c']

sql_insert = """insert into weather (country, city, lat, lon, temp_c, wind_kph, humidity) 
 values ('{0}', '{1}', {2}, {3}, {4}, {5}, {6})""".format(
    result['location']['country'], 
    result['location']['name'], 
    result['location']['lat'], 
    result['location']['lon'], 
    result['current']['temp_c'], 
    result['current']['wind_kph'], 
    result['current']['humidity'])


# В Python, при использовании функции json.dump() или json.dumps() 
# для сериализации данных в формат JSON, по умолчанию параметр 
# ensure_ascii установлен в True. 
# Это означает, что при сериализации текстовых данных, таких как строки, 
# символы Unicode, которые не являются ASCII символами, будут экранированы 
# и преобразованы в символы Unicode Escape (например, "\uXXXX").
with open('weather1.json', 'w', encoding='utf-8') as f:
    json.dump(result, f, indent=4, ensure_ascii=False)

