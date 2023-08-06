from bs4 import BeautifulSoup
import requests


def get_data(url):
    
    gets = requests.get(url)
    soup = BeautifulSoup(gets.text, 'html.parser')
    airs = []
    for tag in soup.find_all('h5'):
        print(tag.text)
        airs.append(tag.text)

    return airs


if __name__ == '__main__':
    url = 'https://zerofromlight.com/blogs'
    print(get_data(url))
