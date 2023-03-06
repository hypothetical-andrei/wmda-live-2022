import requests
import json

# 'https://sg.media-imdb.com/suggests/a/ab.json'

def get_imdb_info(query):
    template = 'https://sg.media-imdb.com/suggests/{first}/{start}.json'
    url = template.format(first = query[0], start = query)
    response = requests.get(url)
    jsonp_data = response.text
    json_data = jsonp_data[8:-1]
    recommendations = json.loads(json_data)
    return recommendations

def main():
    recommendations = get_imdb_info('ab')
    for item in recommendations['d']:
        if item['s'].startswith('Act'):
            print(item['l'])

if __name__ == '__main__':
    main()
