from django.db import models
from django.contrib.auth.models import User


class Food(models.Model):
    name = models.CharField(max_length=300)
    nutri_score = models.CharField(max_length=300)
    web_link = models.CharField(max_length=300)
    place = models.CharField(max_length=300)
    link_food = models.CharField(max_length=300, null=True)

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=300)
    type_category = models.CharField(max_length=300)


class FoodCategory(models.Model):
    food = models.ForeignKey(Food, on_delete=True)
    category = models.ForeignKey(Category, on_delete=True)


class FoodUser(models.Model):
    food = models.ForeignKey(Food, on_delete=True)
    user = models.ForeignKey(User, on_delete=True)

    @classmethod
    def create(cls, food, user):
        food_user = FoodUser.objects.filter(food=food, user=user).count()
        if food_user == 0:
            return cls(food=food, user=user)

    @classmethod
    def get_user_foods(cls, user):
        foods_user = FoodUser.objects.filter(user=user)
        return [ food_user.food for food_user in foods_user]