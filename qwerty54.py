import requests
with open('dataset_3378_3.txt', 'r') as first:
    url = first.read().strip()

    while True:
        r = requests.get(url)
        print(r.text)
        url = 'https://stepic.org/media/attachments/course67/3.6.3/' + r.text


