from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from .config import config_project
from .forms import food_form, user_form, connexion_form
from django.contrib.auth import authenticate, login, logout
from .models import *
from .function import *
from django.contrib.auth.decorators import login_required
import json
import os
from PIL import Image
from io import BytesIO
from .config import config_project
import re


data = {
    'in_mock': config_project['in_mock'],
    'data_header': '',
}


def feed_database(request):
    put_food_in_db()
    load_image()
    return redirect('/website_pur_beurre/home')


def feed_database_heroku(request):
    feed_db_for_heroku()
    return redirect('/website_pur_beurre/home')


def feed_database_by_mock(request):
    put_food_in_db_by_mock()
    return redirect('/website_pur_beurre/home')


def delete_data_from_db(request):
    delete_data_db()
    return redirect('/website_pur_beurre/home')


def load_image_foods(request):
    load_image()
    return redirect('/website_pur_beurre/home')


def home(request):
    data['header'] = False
    data['user'] = request.user
    data['food_form'] = food_form.FoodForm(request.POST)
    redirect('/website_pur_beurre/home')
    return render(request, 'home.html', data)

# --------------------------------------------------------------------------------------------------------------------
# ----------------------------------------------- Gestion utilisateur ------------------------------------------------
# --------------------------------------------------------------------------------------------------------------------


def go_page_connexion(request, error=False):
    data['header'] = False
    data['connexion_form'] = connexion_form.ConnexionForm(request.POST)
    data['error'] = error
    redirect('/website_pur_beurre/home')
    return render(request, 'connexion.html', data)


def connexion(request):
    error = False
    if request.method == "POST":
        form = connexion_form.ConnexionForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            user = authenticate(username=username, password=password)
            if user:
                login(request, user)
            else:
                return go_page_connexion(request, True)
    else:
        form = connexion_form.ConnexionForm()

    redirect('/website_pur_beurre/home')
    return home(request)


def go_inscription(request, errors=[]):
    data['header'] = False
    data['errors'] = errors
    data['user'] = request.user
    data['inscription_form'] = user_form.UserForm(request.POST)
    return render(request, 'inscription.html', data)


def inscription(request):
    errors = []
    if request.method == "POST":
        form = user_form.UserForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["user_name"]
            mail = form.cleaned_data["mail"]
            password = form.cleaned_data["password"]
            password_again = form.cleaned_data["password_again"]
            check_mail = User.objects.filter(email=mail).count()
            check_username = User.objects.filter(username=username).count()

            if check_mail > 0:
                errors.append('Email déja existant.')

            if re.compile("[^@]+@[^@]+\.[^@]+").search(mail) is None:
                errors.append("Email non valide")

            if re.compile("^[A-Za-z0-9]{6,}$").search(password) is None:
                errors.append("Le mot de passe doit contenir au moins 6 caractères")

            if password != password_again:
                errors.append('Les mots de passes ne sont pas identique.')

            if check_username > 0:
                errors.append('Nom utilisateur déja existant.')

            if re.compile("^([A-Za-z1-9]{2,})$").search(password) is None:
                errors.append("Le nom d'utilisateur doit contenir au moins 2 caractères")

            if len(errors) == 0:
                user = User.objects.create_user(username, mail, password)
                user.save()
                login(request, user)
                redirect('/website_pur_beurre/home')
                return home(request)
            else:
                return go_inscription(request, errors)
    redirect('/website_pur_beurre/home')
    return home(request)


def log_out(request):
    data['header'] = False
    logout(request)
    redirect('/website_pur_beurre/home')
    return home(request)


# --------------------------------------------------------------------------------------------------------------------
# --------------------------------------------------- Aliment --------------------------------------------------------
# --------------------------------------------------------------------------------------------------------------------
@csrf_exempt
def search_food(request):
    data['user'] = request.user
    data['header'] = True
    data['error_food'] = False
    if request.method == "POST":
        form = food_form.FoodForm(request.POST)
        if form.is_valid():
            food = form.cleaned_data["food"]
            data['data_header'] = food
            test_exist_food = Food.objects.filter(name=food).count()
            if test_exist_food == 0:
                data['foods'] = {}
                data['error_food'] = True
                data['header'] = False
            else:
                data['food_substituted'] = Food.objects.get(name=food)
                substitute_foods = search_substitue_food(food, request.user.id)
                data['foods'] = substitute_foods

    return render(request, 'result_search_food.html', data)


@csrf_exempt
def save_food(request):
    response = {'error_user_food': False}
    id_food = request.GET.get('id_food')
    if request.user.is_authenticated:
        user = request.user
        food = Food.objects.get(id=id_food)
        nb_food_user = FoodUser.objects.filter(food=food, user=user).count()
        if nb_food_user == 0:
            food_user = FoodUser(food=food, user=user)
            food_user.save()
            response['food'] = food.name
        else:
            response['error_user_food'] = True
    # redirect('/website_pur_beurre/go_page_user_foods')
    return HttpResponse(json.dumps({'food': food.name, 'food_id': food.id}))


@login_required(login_url='go_connexion')
def go_page_user_foods(request):
    data['header'] = False
    data['user'] = request.user
    data['foods'] = []
    if request.user.is_authenticated:
        user = request.user
        foods_user = FoodUser.objects.filter(user=user)
        list_foods = [ food_user.food for food_user in foods_user]
        num_food = 1
        for food in list_foods:
            data['foods'].append({
                'id': food.id,
                'name': food.name,
                'nutri_score': food.nutri_score,
                'web_link': food.web_link,
                'image': str(food.id) + '.png',
                'num_food': num_food % 3,
            })
            num_food += 1
    return render(request, 'my_foods.html', data)


def delete_food(request):
    if request.user.is_authenticated:
        food = Food.objects.get(id=request.GET.get('id_food'))
        user = request.user
        food_user = FoodUser.objects.filter(user=user, food=food)
        food_user.delete()
    return HttpResponse(json.dumps({'food': food.name, 'food_id': food.id}))
    # return go_page_user_foods(request)


@login_required(login_url='go_connexion')
def go_page_food(request, id_food):
    data['header'] = True
    data['user'] = request.user
    data['food'] = Food.objects.get(id=id_food)
    food = Food.objects.get(id=id_food)
    data['data_header'] = food.name
    data['path_image_food'] = str(id_food) + '.png'
    return render(request, 'page_food.html', data)


def get_list_foods():
    json_response = {}
    list_foods = [food for food in Food.objects.all()]
    for food in list_foods:
        json_response['name'] = food.name
        json_response['nutri_score'] = food.nutri_score
    return HttpResponse(json.dumps(json_response))


# --------------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------- Compte ----------------------------------------------------
# --------------------------------------------------------------------------------------------------------------------
@login_required(login_url='go_connexion')
def go_page_account(request):
    data['header'] = True
    data['user'] = request.user
    data['data_header'] = data['user'].username
    return render(request, 'account.html', data)
