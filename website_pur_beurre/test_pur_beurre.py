import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "pur_beurre.settings")
import django ; django.setup()
from .function import check_error_user, search_substitue_food, get_all_type_categories, get_food_with_better_score


class TestData:

    def setup_method(self):
        self.nutriscore = "c"
        self.information = "fr:-\'"
        self.food = "cranberries"
        self.username = "a"
        self.mail = "wrong*email"
        self.password = "h"
        self.password_again = "i"

    def test_check_error_user(self):
        errors = check_error_user(self.username, self.mail, self.password, self.password_again)
        assert len(errors) > 0

    def test_search_substitue_food(self):
        foods = search_substitue_food(self.food, 0, 1)
        assert len(foods) > 0

    def test_get_all_type_categories(self):
        categories = get_all_type_categories()
        assert len(categories) > 0

    def test_get_food_with_better_score(self):
        betters_nutriscore = get_food_with_better_score(self.nutriscore)
        assert betters_nutriscore == "'b','a'" or betters_nutriscore == "'a','b'"

