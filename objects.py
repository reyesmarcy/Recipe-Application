class Category:
    def __init__(self, category):
        self.__category = category

    def get_category(self):
        return self.__category

    def set_category(self, category):
        self.__category = category


class Meal:
    def __init__(self, meal_id, meal, meal_thumb):
        self.__meal_id = meal_id
        self.__meal = meal
        self.__meal_thumb = meal_thumb

    def get_meal_id(self):
        return self.__meal_id

    def set_meal_id(self, meal_id):
        self.__meal_id = meal_id

    def get_meal(self):
        return self.__meal

    def set_meal(self, meal):
        self.__meal = meal

    def get_meal_thumb(self):
        return self.__meal_thumb

    def set_meal_thumb(self, meal_thumb):
        self.__meal_thumb = meal_thumb


class Recipe:
    def __init__(self, meal_id, meal, category, instructions, meal_thumb):
        self.__meal_id = meal_id
        self.__meal = meal
        self.__category = category
        self.__instructions = instructions
        self.__meal_thumb = meal_thumb

    def get_meal_id(self):
        return self.__meal_id

    def set_meal_id(self, meal_id):
        self.__meal_id = meal_id

    def get_meal(self):
        return self.__meal

    def set_meal(self, meal):
        self.__meal = meal

    def get_category(self):
        return self.__category

    def set_category(self, category):
        self.__category = category

    def get_instructions(self):
        return self.__instructions

    def set_instructions(self, instructions):
        self.__instructions = instructions

    def get_meal_thumb(self):
        return self.__meal_thumb

    def set_meal_thumb(self, meal_thumb):
        self.__meal_thumb = meal_thumb


class Area:
    def __init__(self, area):
        self.__area = area

    def get_area(self):
        return self.__area

    def set_area(self, area):
        self.__area = area


