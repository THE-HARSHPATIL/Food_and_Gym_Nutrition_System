from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('',views.navbar2,name="navbar2"),
    path('about',views.about,name="about"),
    path('Bmi_new',views.Bmi_new,name="Bmi_new"),
    path('Food',views.Food,name="Food"),
    path('Calories',views.Calories,name="Calories"),
]
