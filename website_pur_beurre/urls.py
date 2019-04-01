from django.urls import path
from . import views

urlpatterns = [
    path('home', views.home, name="home"),
    path('', views.home, name="home"),
    # ------------------- database -------------------
    path('feed_database', views.feed_database, name="feed_database"),
    path('feed_database_heroku', views.feed_database_heroku, name="feed_database_heroku"),
    path('feed_database_by_mock', views.feed_database_by_mock, name="feed_database_by_mock"),
    path('delete_data_from_db', views.delete_data_from_db, name="delete_data_from_db"),

    # ------------------- authentication -------------------
    path('go_connexion', views.go_page_connexion, name="go_connexion"),
    path('connexion', views.connexion, name="connexion"),
    path('go_inscription', views.go_inscription, name="go_inscription"),
    path('inscription', views.inscription, name="inscription"),
    path('logout', views.log_out, name="logout"),

    # ------------------- Users -------------------
    path('go_page_account', views.go_page_account, name="go_page_account"),
    path('go_page_user_foods', views.go_page_user_foods, name="go_page_user_foods"),
    path('update_account', views.update_account, name="update_account"),

    # ------------------- Foods -------------------
    path('load_image_foods', views.load_image_foods, name="load_image_foods"),
    path('search_food/<int:num_page>', views.search_food, name="search_food"),
    path('search_food_by_page/<str:food_name>/<int:num_page>', views.search_food_by_page, name="search_food_by_page"),
    path('save_food', views.save_food, name="save_food"),
    path('delete_food', views.delete_food, name="delete_food"),
    path('go_page_food/<int:id_food>', views.go_page_food, name="go_page_food"),
    path('get_list_foods', views.get_list_foods, name="get_list_foods"),

]