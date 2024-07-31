from django.shortcuts import render, get_object_or_404, get_list_or_404
from .models import Recipe
from django.http import Http404
from django.db.models import Q

def home(request):
    recipes = get_list_or_404(Recipe.objects.filter(is_published=True,).order_by('-id'))
    return render(request,'recipes/pages/home.html', {'recipes': recipes})

def category(request, category_id):
    recipes = get_list_or_404(Recipe.objects.filter(category__id=category_id, is_published=True,).order_by('-id'))
    
    
    
    return render(request,'recipes/pages/category.html', {'recipes': recipes, 'title': f'{recipes[0].category.name}'})


def recipe(request, id):
    recipe = get_object_or_404(Recipe, id=id, is_published=True)
    
    return render(request,'recipes/pages/recipe-view.html', {'is_detail_page': True, 'recipe': recipe,})


def search(request):
    search_term = request.GET.get('q', '').strip()
    
    if not search_term:
        raise Http404()
    
    recipes = Recipe.objects.filter(Q(title__icontains=search_term) | Q(description__icontains=search_term)).order_by('-id')
    
    return render (request, 'recipes/pages/search.html', {'page_title': f'Search for "{search_term}"', 'search_term': search_term, 'recipes': recipes})