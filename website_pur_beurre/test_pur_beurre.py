import pytest
from .function import *
import json
from urllib2 import urlopen


class TestDataBase:
    def setup_method(self):
        self.dbname = config_project['db']['dbname']
        self.user = config_project['db']['user']
        self.host = config_project['db']['host']
        self.password = config_project['db']['password']
        self.connect_is_work = True
        self.insert = True
        self.cursor = get_connection_db().cursor()

    def teardown_function(self):
        request_delete_food = "DELETE FROM website_pur_beurre_food WHERE name = 'food_name'"
        self.cursor.execute(request_delete_food)
        request_delete_category = "DELETE FROM website_pur_beurre_category WHERE name = 'category_name'"
        self.cursor.execute(request_delete_category)

    def test_connexion(self):
        try:
            psycopg2.connect(dbname=self.dbname,
                             user=self.user,
                             host=self.host,
                             password=self.password)
        except psycopg2.OperationalError:
            self.connect_is_work = False

        assert self.connect_is_work is True

    def test_insert_food(self):
        try:
            request_insert_food = "INSERT INTO website_pur_beurre_food (name, nutri_score, web_link, place, link_food) " \
                             "VALUES ('food_name', 'nutrition_grade', 'url', 'place','image');"
            self.cursor.execute(request_insert_food)

            query_insert_category = "INSERT INTO website_pur_beurre_category (name, type_category) " \
                                    "VALUES ('category_name', 'category_type');"
            self.cursor.execute(query_insert_category)
        except psycopg2.OperationalError:
            self.insert = False

        assert self.insert is True


class TestData:
    def setup_method(self):
        self.path = "/ * \\"
        self.nutriscore = "c"
        self.information = "fr:-\'"

    def test_clean_data(self):
        self.information = clean_data(self.information)
        assert self.information == '-'

    def test_adapt_name_for_path(self):
        self.path = adapt_name_for_path(self.path)
        assert self.path == "- x -"

    def test_get_food_with_better_score(self):
        betters_nutriscore = get_food_with_better_score(self.nutriscore)
        assert betters_nutriscore == "'b','a'" or betters_nutriscore == "'a','b'"

    def test_mock(self, monkeypatch):
        json_data = json.load(open("data_mock.json"))

        def mockreturn(request):
            return json.dumps(json_data)

        monkeypatch.setattr(urllib.request, 'urlopen', mockreturn)

        local_res = json.load(open("data_mock.json"))

        assert len(local_res["Cookies"]["products"]) > 0
