from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView
from .src.recipe.analyze_recipe import getRecipe
from .src.recipe.search_recipesURL import getURL

# Create your views here.
def index(request):
    return render(request, 'template.html')


class searchView(TemplateView):
    def __init__(self):
        self.params={
            'title':'レシピ検索',
            'dish name':None,
            'data':[]
        }

    def get(self,request):
        return render(request,'templates/recipe/search_recipes.html',self.params)

    def post(self,request):
        self.params['data']=getURL(request.POST['dish name'])
        return render(request,'templates/recipe/search_recipes.html',self.params)

