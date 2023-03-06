import requests
from pyquery import PyQuery as pq

headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36'
}

url = 'https://www.themoviedb.org/movie/785084-the-whale'
response = requests.get(url, headers=headers)
html = response.text

dom = pq(html)

elements = dom('.facts p')
element_contents = [pq(e).text() for e in elements]

for content in element_contents:
    items = content.split('\n')
    if items[0] == 'Budget':
        print('Budget : ', items[1])
    if items[0] == 'Revenue':
        print('Revenue : ', items[1])

