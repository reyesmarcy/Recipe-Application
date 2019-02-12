from urllib import request, parse
import json

from objects import Category, Meal, Recipe, Area


# Get a list of the meal categories
def get_categories():
    url = 'https://www.themealdb.com/api/json/v1/1/list.php?c=list'
    f = request.urlopen(url)
    categories = []

    try:
        data = json.loads(f.read().decode('utf-8'))
        for category_data in data['meals']:
            category = Category(category_data['strCategory'])

            categories.append(category)
    except (ValueError, KeyError, TypeError):
        print("JSON format error")

    return categories


# List all meals by category
def get_meals_by_category(category):
    url = 'https://www.themealdb.com/api/json/v1/1/filter.php?c=' + category
    f = request.urlopen(url)
    meals = []

    try:
        data = json.loads(f.read().decode('utf-8'))
        for meal_data in data['meals']:
            category = Meal(meal_data['idMeal'],
                            meal_data['strMeal'],
                            meal_data['strMealThumb'])

            meals.append(category)
    except (ValueError, KeyError, TypeError):
        print("JSON format error")

    return meals


# Search a meal by Name
def get_meal_by_name(meal):
    url = 'https://www.themealdb.com/api/json/v1/1/search.php?s=' + parse.quote(meal)
    f = request.urlopen(url)

    recipe = None
    try:
        data = json.loads(f.read().decode('utf-8'))

        for recipe_data in data['meals']:
            recipe = Recipe(recipe_data['idMeal'],
                            recipe_data['strMeal'],
                            recipe_data['strCategory'],
                            recipe_data['strInstructions'],
                            recipe_data['strMealThumb'])

    except (ValueError, KeyError, TypeError):
        print("JSON format error")

    return recipe


def get_areas():
    url = 'https://www.themealdb.com/api/json/v1/1/list.php?a=list'
    f = request.urlopen(url)
    areas = []

    try:
        data = json.loads(f.read().decode('utf-8'))
        for area_data in data['meals']:
            area = Area(area_data['strArea'])

            areas.append(area)

    except (ValueError, KeyError, TypeError):
        print("JSON format error")

    return areas


def get_meals_by_area(area):
    url = 'https://www.themealdb.com/api/json/v1/1/filter.php?a=' + area
    f = request.urlopen(url)
    meals = []

    try:
        data = json.loads(f.read().decode('utf-8'))
        for meal_data in data['meals']:
            area = Meal(meal_data['idMeal'],
                        meal_data['strMeal'],
                        meal_data['strMealThumb'])

            meals.append(area)
    except (ValueError, KeyError, TypeError):
        print("JSON format error")

    return meals

