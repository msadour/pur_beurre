from django.urls import path
from . import views

urlpatterns = [
    path('home', views.home),
    path('go_connexion', views.go_page_connexion, name="go_connexion"),
    path('connexion', views.connexion, name="connexion"),
    path('inscription', views.inscription, name="inscription"),
    path('logout', views.log_out, name="logout"),
    path('feed_database', views.feed_database, name="feed_database"),
    path('go_page_account', views.go_page_account, name="go_page_account"),
    path('search_food', views.search_food, name="search_food"),
    path('save_food', views.save_food, name="save_food"),
    path('go_page_user_foods', views.go_page_user_foods, name="go_page_user_foods"),
    path('delete_food', views.delete_food, name="delete_food"),
    path('go_page_food/<int:id_food>', views.go_page_food, name="go_page_food"),
    path('get_list_foods', views.get_list_foods, name="get_list_foods"),
]