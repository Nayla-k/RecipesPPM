from django.shortcuts import render, HttpResponse
from . import models
recipes = [{

}]

def home(request):
  recipes = models.Recipe.objects.all()
  context = {
    'recipes': recipes
  }
  return render(request, "recipes/home.html")



def about(request):
  return render(request,"recipes/about.html")