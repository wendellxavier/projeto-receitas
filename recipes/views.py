from django.shortcuts import render
from .models import Recipe

def home(request):
    recipes = Recipe.objects.filter(is_published=True).order_by('-id')
    return render(request,'recipes/pages/home.html', {'recipes': recipes})

def category(request, category_id):
    recipes = Recipe.objects.filter(category__id=category_id, is_published=True).order_by('-id')
    return render(request,'recipes/pages/category.html', {'recipes': recipes})


def recipe(request, id):
    return render(request,'recipes/pages/recipe-view.html', {'is_detail_page': True, 'recipe': recipe,})
