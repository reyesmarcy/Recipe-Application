#! /usr/bin/env python
import requests


def show_title():
    # This method displays the title to screen
    print("My Recipes Program")
    print()


def show_menu():
    # This method displays the menu to screen
    print("COMMAND MENU")
    print("1 - List all Categories")
    print("2 - List all Meals for a Category")
    print("3 - Search Meal by Name")
    print("4 - List all Areas")
    print("5 - List all Meals for an Area")
    print("0 - Exit the Program")
    print()


def list_categories(categories):
    # This method displays the list of categories to screen
    print("CATEGORIES")
    for i in range(len(categories)):
        category = categories[i]
        print(category.get_category())
    print()


def list_meals_by_category(category, meals):
    # This method displays the list of meals to screen
    print(category.upper() + " MEALS")
    for i in range(len(meals)):
        meal = meals[i]
        print(meal.get_meal())
    print()


def search_meal_by_category(categories):
    """
        This method is used to get a category to search for meals on
        and then make the call to get the list of meals for the category
    """

    lookup_category = input("Enter a Category: ")
    found = False

    # Validate Categories
    for i in range(len(categories)):
        category = categories[i]
        if category.get_category().lower() == lookup_category.lower():
            found = True
            break

    if found:
        meals = requests.get_meals_by_category(lookup_category)
        list_meals_by_category(lookup_category, meals)
    else:
        print("Invalid category, please try again.\n")


def display_meal(recipe):
    # This method is used to display the meal information to screen
    print()
    print("Recipe:", recipe.get_meal())
    print("Instructions:", recipe.get_instructions())
    print()


def search_meal_by_name():
    """
        This method is used to get a meals name from the user and
        make the call to get the meal from the site
    """
    lookup_meal = input("Enter Meal Name: ")

    meal = requests.get_meal_by_name(lookup_meal)
    if meal:
        display_meal(meal)
    else:
        print("A recipe for this meal was not found.\n")


def list_areas(areas):
    # This method displays the list of areas to screen
    print("AREAS")
    for i in range(len(areas)):
        area = areas[i]
        print(area.get_area())
    print()


def list_meals_by_area(area, meals):
    # This method displays the list of meals to screen
    print(area.upper() + " MEALS")
    for i in range(len(meals)):
        meal = meals[i]
        print(meal.get_meal())
    print()


def search_meal_by_area(areas):
    """
        This method is used to get a category to search for meals on
        and then make the call to get the list of meals for the category
    """

    lookup_area = input("Enter an area: ")
    found = False

    # Validate areas
    for i in range(len(areas)):
        area = areas[i]
        if area.get_area().lower() == lookup_area.lower():
            found = True
            break

    if found:
        meals = requests.get_meals_by_area(lookup_area)
        list_meals_by_area(lookup_area, meals)
    else:
        print("Invalid area, please try again.\n")


def main():
    # This method controls the flow of the program

    #Show the title and menu to screen
    show_title()
    show_menu()

    # Get the list of categories
    categories = requests.get_categories()
    areas = requests.get_areas()

    # Get the user menu selection
    while True:
        command = input("Command: ")
        if command == "1":
            list_categories(categories)
        elif command == "2":
            search_meal_by_category(categories)
        elif command == "3":
            search_meal_by_name()
        elif command == "4":
            list_areas(areas)
        elif command == "5":
            search_meal_by_area(areas)
        elif command == "0":
            print("Cya!")
            break
        else:
            print("Not a valid command. Please try again.\n")


if __name__ == "__main__":
    main()