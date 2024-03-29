from django.shortcuts import get_object_or_404, render, redirect

from .models import Recipe

# Create your views here.
def index(request):
    latest_recipes = Recipe.objects.order_by("-created_date")[:5]
    print(latest_recipes)
    context = {
        "latest_recipes": latest_recipes
    }
    return render(request, "web/index.html", context)

def recipe(request, recipe_id):
    recipe = get_object_or_404(Recipe, pk=recipe_id)
    return render(request, "web/recipe.html", { "recipe": recipe})

def recipes(request):
    if request.method == "POST":
        try:
            print(request.POST["title"])
            return redirect("index")
        except:
            return redirect("index")
    if request.method == "GET":
        return redirect("index")

def recipe_form(request, recipe_id=None):
    if recipe_id:
        recipe = get_object_or_404(Recipe, pk=recipe_id)
        return render(request, "web/recipe_form.html", { "recipe": recipe })
    
    return render(request, "web/recipe_form.html")
