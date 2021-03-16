from urllib.request import urlopen
from urllib.error import HTTPError
from urllib.parse import quote
from bs4 import BeautifulSoup


def getURL(dishName):
    url="https://cookpad.com/search/"
    url+=quote(dishName)
    try:
        html = urlopen(url)
    except HTTPError:
        return None
    try:
        html = urlopen(url)
        bs = BeautifulSoup(html, 'html.parser')
        label_list = bs.find_all(class_="dish_label")
        if len(label_list):
            result_list=["label"]
            for i in label_list:
                result_list.append(i.get_text())
            return label_list
        title_list=bs.find_all(class_="recipe-title font13")
        discription_list=bs.find_all(class_="recipe_description")
        material_list=bs.find_all(class_="material ingredients")
        link_list=bs.find_all(class_="recipe-title font13")
        result_list=[]
        for i,j,k,l in zip(title_list,discription_list,material_list,link_list):
            result_list.append([i.get_text(),j.get_text()[1:-1],k.get_text()[6:-1],"https://cookpad.com"+l.get("href")])
        return result_list
    except AttributeError:
        return None

def getURLfromLabel(url):
    try:
        html = urlopen(url)
    except HTTPError:
        return None
    try:
        html = urlopen(url)
        bs = BeautifulSoup(html, 'html.parser')
        title_list=bs.find_all(class_="recipe-title font13")
        discription_list=bs.find_all(class_="recipe_description")
        material_list=bs.find_all(class_="material ingredients")
        link_list=bs.find_all(class_="recipe-title font13")
        result_list=[]
        for i,j,k,l in zip(title_list,discription_list,material_list,link_list):
            result_list.append([i.get_text(),j.get_text()[1:-1],k.get_text()[6:-1],"https://cookpad.com"+l.get("href")])
        return result_list
    except AttributeError:
        return None