import requests
line = 0
with open('dataset_3378_2.txt', 'r') as text:
    url_in_file = text.read().strip()
    text_in_file = requests.get(url_in_file)
    text_in_file.text.splitlines()
    x = text_in_file.text.count('\n')
    print(x)
