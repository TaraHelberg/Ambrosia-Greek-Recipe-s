from . import views
from django.urls import path

urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path('browse/', views.RecipeList.as_view(), name='browse'),
    path('<slug:slug>/', views.RecipeDetail.as_view(), name='recipe_detail'),
]
