from django.shortcuts import render
from . import views
from mini.models import vegetables,bakery_products,milk_products,fruits,dry_fruits,meat_eggs_fishes


def navbar2(request):
    return render(request,'navbar2.html')

def about(request):
    return render(request,'about.html')

def Bmi_new(request):
    return render(request,'Bmi_new.html')

def Food(request):
    veg=vegetables.objects.all()
    bak=bakery_products.objects.all()
    milk=milk_products.objects.all()
    frut=fruits.objects.all()
    dry=dry_fruits.objects.all()
    meat=meat_eggs_fishes.objects.all()
    data={
        'veg1' : veg,
        'bak1' : bak,
        'milk1': milk,
        'frut1': frut,
        'dry1' : dry,
        'meat1' : meat
    }
    
    return render(request,'Food.html',data)

def Calories(request):
    return render(request,'Calories.html')
