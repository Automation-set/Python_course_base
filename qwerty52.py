import requests

r = requests.get('http://example.com') # Простой Get запрос
print(r.text) # Вывод ответа от сервера

url = 'http://example.com'
par = {'key1': 'value1', 'key2': 'value2'}
r = requests.get(url, params=par) # Передача параметров в запрос
print(r.url) # Сформированный url-адрес с учетом параметров GET запроса

url = 'http://httpbin.org/cookies'
cookies = {'cookies_are': 'working'}
r = requests.get(url, cookies=cookies) # Отправка сформированных cookies на сервер

print(r.cookies['example_cookies_name']) # Использование cookies, полученных от сервера
