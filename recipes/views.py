from django.shortcuts import render
from django.views import generic
from .models import Recipe


class Home(generic.TemplateView):
    """
    Home page view
    """
    template_name = "index.html"


class RecipeList(generic.ListView):
    model = Recipe
    queryset = Recipe.objects.filter(status=1).order_by('-created_on')
    template_name = 'browse.html'
    paginate_by = 6
