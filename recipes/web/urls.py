from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("recipes/new/", views.recipe_form, name="new_recipe"),
    path("recipes/", views.recipes, name="recipes"),
    path("recipes/<int:recipe_id>/", views.recipe, name="recipe"),
    path("recipes/<int:recipe_id>/edit", views.recipe_form, name="edit_recipe")
]