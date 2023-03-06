import requests
from pyquery import PyQuery as pq

# url = 'https://en.wikipedia.org/wiki/Romanian_leu'
url = 'https://en.wikipedia.org/wiki/Swedish_krona'
response = requests.get(url)
html = response.text

dom = pq(html)
code = 'n/a'

elements = dom('.infobox tr')

for element in elements:
    element_dom = pq(element)
    label_element = element_dom('.infobox-label')
    if pq(label_element).text() == 'Code':
        code = element_dom('.infobox-data').text()
        break

print(code.split(' ')[0])