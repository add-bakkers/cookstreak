from django.urls import path
from django.conf.urls import url
from .views import searchView
from .views import index

urlpatterns = [
    path('search/', searchView.as_view(),name='search'),
]