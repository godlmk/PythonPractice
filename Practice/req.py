import requests
from bs4 import BeautifulSoup


if __name__ == '__main__':
    url = "http://www.python123.io/ws/demo.html"
    r = requests.get(url)
    demo = r.text
    soup = BeautifulSoup(demo, "html.parser")
    print(soup.p.prettify())
