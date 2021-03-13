from urllib.request import urlopen
from urllib.error import HTTPError
from bs4 import BeautifulSoup


def getRecipe(url):
    try:
        html = urlopen(url)
    except HTTPError as e:
        return None
    try:
        html = urlopen(url)
        bs = BeautifulSoup(html, 'html.parser')
        nameList = bs.find_all(class_="step_text")
        for name in nameList:
            print(name.get_text())
    except AttributeError as e:
        return None
    return title