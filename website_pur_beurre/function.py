"""
Contain the class for run application.
"""

import psycopg2
import requests
from decimal import Decimal
from .config import config_project
from PIL import Image
import requests
from io import BytesIO
import os


def get_connection_db():
    """
    Get a connexion of database
    :return: connexion
    """
    connexion = psycopg2.connect(dbname=config_project['db']['dbname'],
                                 user=config_project['db']['user'],
                                 host=config_project['db']['host'],
                                 password=config_project['db']['password']
                                 )
    return connexion


def get_food_with_better_score(current_score):
    """
    Return a list (string) with better score than a score of food what we want replace
    :return:
    """
    list_better_score = []
    better_score_str = ''
    table_nutri_score = {'a': 5, 'b': 4, 'c': 3, 'd': 2, 'e': 1}
    score_my_food = table_nutri_score[current_score]
    if score_my_food == 5:
        list_better_score.append('a')
    else:
        for letter, score in table_nutri_score.items():
            if score > score_my_food and score not in [2, 1]:
                list_better_score.append(letter)
    for letter in list_better_score:
        better_score_str = better_score_str + "'" + letter + "',"
    # for delete the last comma :
    better_score_str = better_score_str[:-1]
    return better_score_str


def sort_dict(dict_no_sorted, sens="asc"):
    """
    This function sort a dict by theses keys.
    :return:
    """

    dict_sorted = {}
    lst_keys = sorted([int(key) for key, value in dict_no_sorted.items()])
    if sens == "desc":
        lst_keys = reversed(lst_keys)
    for k in lst_keys:
        value_sorted = dict_no_sorted[str(k)]
        dict_sorted[k] = value_sorted
    return dict_sorted


def make_dict_element(cursor, request, index=None, is_row=False, list_index=None):
    """
    Make a dictionnary with sorted keys (number who a user input) and them values
    for display a number with them value like this : 1 - value ..
    :return: Dictionnary with sorted keys
    """
    cursor.execute(request)
    list_element = {}
    num_element = 1
    list_name_element = []
    for element in cursor.fetchall():
        if not is_row:
            list_name_element.append(element[index])
        else:
            # import pdb ; pdb.set_trace()
            tuple_element = tuple((element[i] for i in list_index))
            list_name_element.append(tuple_element)

    for element in sorted(list_name_element):
        list_element[str(num_element)] = element
        num_element += 1

    list_element = sort_dict(list_element)
    return list_element


def clean_data(data):
    """
    In some case, some data content character which can not display on the application. This method
    remove bad character in a data name.
    :return: cleaned_data
    """
    if data[:3] in ['it:', 'fr:', 'en:', 'es:', 'de:']:
        data = data[3:]
    if data[:4] in [' it:', ' fr:', ' en:', ' es:', ' de:']:
        data = data[4:]
    if '\'' in data:
        data = data.replace('\'', '')
    if data[:1] == ' ':
        data = data[1:]

    return data


def adapt_name_for_path(data):
    if '/' in data:
        data = data.replace('/', '-')
    if '*' in data:
        data = data.replace('*', 'x')
    return data


def search_substitue_food(food):
    """
    Display all categories and when a user select a categorie, all food with
    them categorie is display. When user selected a food, all substitute of them
    food (with better score) is display and he can replace this food or not.
    :return:
    """
    connexion = get_connection_db()
    cursor = connexion.cursor()

    query_category = "SELECT website_pur_beurre_Category.name " \
                     "FROM website_pur_beurre_Category, website_pur_beurre_FoodCategory, website_pur_beurre_Food " \
                     "WHERE website_pur_beurre_Category.id = website_pur_beurre_FoodCategory.category_id " \
                     "AND website_pur_beurre_Food.id = website_pur_beurre_FoodCategory.food_id " \
                     "AND website_pur_beurre_Food.name = '" + food + "'"

    cursor.execute("SELECT nutri_score FROM website_pur_beurre_Food WHERE name = '" + food + "';")
    list_betters_score = get_food_with_better_score(cursor.fetchone()[0])

    query_better_food = \
        "SELECT DISTINCT website_pur_beurre_Food.id, website_pur_beurre_Food.name, website_pur_beurre_Food.nutri_score " \
        ", website_pur_beurre_Food.web_link, website_pur_beurre_Food.link_food " \
        "FROM website_pur_beurre_Category, website_pur_beurre_Food, website_pur_beurre_FoodCategory " \
        "WHERE website_pur_beurre_category.id = website_pur_beurre_FoodCategory.category_id " \
        "AND website_pur_beurre_food.id = website_pur_beurre_FoodCategory.food_id " \
        "AND website_pur_beurre_Category.name IN (" + query_category + ") " \
        "AND nutri_score IN ( " + list_betters_score + ") AND website_pur_beurre_Food.name != '" + food + "'" \
                                                                                                          "LIMIT 6;"

    foods_substitute = make_dict_element(cursor, query_better_food, 0, is_row=True, list_index=[0, 1, 2, 3, 4])
    return foods_substitute


def get_user_foods(connexion, id_user):
    """
    Select the food what user selected.
    :return: list of the food what user replaced
    """
    cursor = connexion.cursor()
    query_select_food_user = "SELECT * " \
                             "FROM website_pur_beurre_Food, website_pur_beurre_FoodUser " \
                             "WHERE website_pur_beurre_Food.id = website_pur_beurre_FoodUser.food_id " \
                             "AND website_pur_beurre_FoodUser.id_user = " + str(id_user) + ";"
    cursor.execute(query_select_food_user)
    if cursor.fetchone() is None:
        return {}
    else:
        users_foods = make_dict_element(cursor,
                                             query_select_food_user,
                                             None,
                                             True,
                                             [1, 2, 3, 4])
        return users_foods


def put_food_in_db():
    """
    Get json files for put elements in database.
    :return:
    """

    connexion = get_connection_db()

    list_type_category = [
        'Aliments à base de fruits et de légumes',
        'Cookies',
        'Desserts glacés',
        'Fruits',
        'Gâteaux',
        'Hamburgers',
        'Pâtes à tartiner',
        'Produits de la mer',
        'Sandwichs',
        'Viandes',
    ]

    for type_category in list_type_category:
        print(type_category + " - " + str(list_type_category.index(type_category) + 1) + '/' + str(len(list_type_category)))
        print("-------------------------------")
        cursor = connexion.cursor()

        type_category = type_category.lower()
        first_page = requests.get(
            'https://fr-en.openfoodfacts.org/category/'+type_category+'/1.json').json()
        page_size = first_page['page_size']
        count_element = first_page['count']
        total_page = Decimal(round(count_element / page_size, 0)) + 2
        food_category = {}
        list_categories_in_db = []
        list_food_in_db = []
        for num_page in range(1, int(total_page)):
            foods = requests.get(
                'https://fr-en.openfoodfacts.org/category/'+type_category+'/' + str(num_page)+'.json').json()
            for food in foods['products']:
                # Products wihout nutrition grades not will insert in database.
                if 'nutrition_grades' in food.keys():
                    if 'product_name_fr' not in food.keys():
                        product_name = clean_data(food['product_name'])
                    else:
                        product_name = clean_data(food['product_name_fr'])

                    product_place = ''
                    if 'purchase_places' in food.keys():
                        product_place = clean_data(product_place)

                    if product_name.lower() not in list_food_in_db:
                        list_food_in_db.append(product_name.lower())
                        if product_name != '':
                            link_food = 'http://www.idfmoteurs.com/images/pas-image-disponible.png'
                            if food.get('image_front_small_url'):
                                link_food = food['image_front_small_url']

                            try:
                                image_food = Image.open(BytesIO(requests.get(link_food).content))
                            except OSError:
                                link_food = 'http://www.idfmoteurs.com/images/pas-image-disponible.png'
                                image_food = Image.open(BytesIO(requests.get(link_food).content))
                            finally:
                                image_food.thumbnail((128, 128), Image.ANTIALIAS)
                                current_directory = os.path.dirname(os.path.realpath(__file__))
                                name_for_path = adapt_name_for_path(product_name.lower())
                                image_food.save(current_directory + '\\static\\img\\foods\\' + name_for_path + '.png',
                                                "PNG")
                                request_insert = "INSERT INTO website_pur_beurre_food (name, nutri_score, web_link, place, link_food) " \
                                                 "VALUES ('" + product_name.lower() + "', '" \
                                                 + food['nutrition_grades'] + "', '"\
                                                 + food['url'] + "', '" + product_place.lower() + "', '" + link_food + "');"
                                cursor.execute(request_insert)

                            food_category[product_name] = []
                            # for each product, we get all categories which product is associate
                            list_categories = food['categories'].split(',')
                            list_categories = [category.lower() for category in list_categories]
                            for category in list_categories:
                                category = clean_data(category)
                                if category not in list_categories_in_db:
                                    # We check if category is not exist for insert it
                                    list_categories_in_db.append(category)
                                    query_insert_category = "INSERT INTO website_pur_beurre_category (name, type_category) " \
                                                            "VALUES ('" + category.lower() + "', '"+type_category.lower()+"');"
                                    cursor.execute(query_insert_category)
                                food_category[product_name].append(category)

                        connexion.commit()

                    # We associate each food with them categories
                    if product_name != '':
                        for food, list_category in food_category.items():
                            query_get_food = "SELECT id FROM website_pur_beurre_Food WHERE name = '" + product_name.lower() + "';"
                            cursor.execute(query_get_food)
                            food_id = cursor.fetchone()[0]
                            if food_id:
                                for category in list_category:
                                    cursor.execute("SELECT id FROM website_pur_beurre_Category WHERE name = '" + category.lower() + "';")
                                    for category_id in cursor.fetchall():
                                        cursor.execute("SELECT * "
                                                       "FROM website_pur_beurre_FoodCategory "
                                                       "WHERE food_id = '" + str(food_id) + "'"
                                                       "AND category_id = '" + str(category_id[0]) + "';")
                                        # We check if we don't have the same food associate at the same category
                                        if cursor.fetchone() is None:

                                            request_put_food_category = "INSERT INTO website_pur_beurre_FoodCategory" \
                                                                        "(food_id, category_id) " \
                                                                    "VALUES (" + str(food_id) + ", " \
                                                                    + str(category_id[0]) + ");"
                                            cursor.execute(request_put_food_category)
                        connexion.commit()
