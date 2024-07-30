from django.test import TestCase
from django.urls import reverse, resolve

from recipes import views

class RecipeViewsTest(TestCase):
    def test_recipe_home_view_fuction_is_correct(self):
        view = resolve(reverse('recipes:home'))
        self.assertIs(view.func, views.home)
        
    def test_recipe_category_view_fuction_is_correct(self):
        view = resolve(reverse('recipes:category', kwargs={'category_id': 1}))
        self.assertIs(view.func, views.category)
        
    def test_recipe_recipe_detail_view_fuction_is_correct(self):
        view = resolve(reverse('recipes:recipe', kwargs={'id': 1}))
        self.assertIs(view.func, views.recipe)


    def test_recipe_home_view_returns_status_code_200_ok(self):
        response = self.client.get(reverse('recipes:home'))
        self.assertEqual(response.status_code, 200)
        
    def test_recipe_home_view_loads_correct_templates(self):
        response = self.client.get(reverse('recipes:home'))
        self.assertTemplateUsed(response, 'recipes/pages/home.html')
        
    def test_recipe_home_template_shows_no_recipes_found_if_no_recipes(self):
        reponse = self.client.get(reverse('recipes:home'))
        self.assertIn('<h1>No recipes found here</h1>', reponse.content.decode('utf-8'))
    
    def test_recipe_search_uses_correct_view_function(self):
        resolved = reverse(reverse('recipes:search'))
        self.assertIs(resolved.func, views.search)
        
    def test_recipe_search_raises_404_if_no_search_term(self):
        reponse = self.client.get(reverse('recipes:home'))
        self.assertEqual(reponse.status_code, 404)
        