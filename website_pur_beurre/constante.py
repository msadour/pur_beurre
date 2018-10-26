# ---------------------------------------------- DATABASE ----------------------------------------------
# --- Food ---
TABLE_FOOD = "website_pur_beurre_Food"
FOOD_ID = "website_pur_beurre_Food.id"
FOOD_NAME = "website_pur_beurre_Food.name"
FOOD_WEBLINK = "website_pur_beurre_Food.web_link"
FOOD_NUTRISCORE = "website_pur_beurre_Food.nutri_score"
FOOD_LINKFOOD = "website_pur_beurre_Food.link_food"
FOOD_PLACE = "website_pur_beurre_Food.place"


# --- Category ---
TABLE_CATEGORY = "website_pur_beurre_Category"
CATEGORY_ID = "website_pur_beurre_Category.id"
CATEGORY_NAME = "website_pur_beurre_Category.name"
CATEGORY_TYPE = "website_pur_beurre_Category.type_category"

# --- Food_category ---
TABLE_FOOD_CATEGORY = "website_pur_beurre_FoodCategory"
FOOD_CATEGORY_FOOD_ID = "website_pur_beurre_FoodCategory.food_id"
FOOD_CATEGORY_CATEGORY_ID = "website_pur_beurre_FoodCategory.category_id"

# --- Food_user ---
TABLE_FOOD_USER = "website_pur_beurre_Fooduser"
TABLE_FOOD_USER_FOOD_ID = "website_pur_beurre_Fooduser.food_id"
TABLE_FOOD_USER_USER_ID = "website_pur_beurre_Fooduser.user_id"

DB_HEROKU = "postgres://kfwcgmbpgmbjqd:5f1fe7a35757878232fe2f8d3c42904617590c9e7790eed29ab0569576492a88@ec2-54-228-251-254.eu-west-1.compute.amazonaws.com:5432/da4492tmntkdhv"


# ---------------------------------------------- Image ----------------------------------------------
IMAGE_NOT_FOUND = "http://www.idfmoteurs.com/images/pas-image-disponible.png"

# ---------------------------------------------- Link ----------------------------------------------
LINK_OPENFOODFACTS = "https://fr-en.openfoodfacts.org/category/"
LINK_OPENFOODFACTS_CATEGORIES = "https://fr.openfoodfacts.org/categories.json"