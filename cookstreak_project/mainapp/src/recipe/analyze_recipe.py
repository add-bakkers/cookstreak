from urllib.request import urlopen
from urllib.error import HTTPError
from bs4 import BeautifulSoup


def getRecipe(url):
    try:
        html = urlopen(url)
    except HTTPError:
        return None
    try:
        html = urlopen(url)
        bs = BeautifulSoup(html, 'html.parser')
        procedure_list = bs.find_all(class_="step_text")
        return procedure_list
    except AttributeError:
        return None