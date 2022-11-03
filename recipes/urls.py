from . import views
from django.urls import path

urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path('browse/', views.RecipeList.as_view(), name='browse'),
    path('add_recipe/', views.AddRecipe.as_view(), name='add_recipe'),
    path('<slug:slug>/', views.RecipeDetail.as_view(), name='recipe_detail'),
    path('like/<slug:slug>', views.RecipeLike.as_view(), name='recipe_like'),
    path('update/<int:pk>', views.UpdateRecipe.as_view(), name='update'),
    path('delete/<int:pk>', views.DeleteRecipe.as_view(), name='delete'),
]
