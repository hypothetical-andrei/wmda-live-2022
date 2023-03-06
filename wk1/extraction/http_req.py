import requests

def get_content(url):
    response = requests.get(url)
    return response.text

def main():
    content = get_content('http://andrei.ase.ro')
    print(content)

if __name__ == '__main__':
    main()