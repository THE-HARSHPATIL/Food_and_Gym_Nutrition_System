from django.db import models

class vegetables(models.Model):  
    id = models.IntegerField(primary_key=True)  
    Vegetable_name = models.CharField(max_length=100)  
    Portion_size_per_100g = models.CharField(max_length=100)  
    Calories = models.IntegerField()
    Nutritional_content = models.CharField(max_length=200)  
    class Meta:  
        db_table = "vegetables" 
        
class bakery_products(models.Model):  
    id = models.IntegerField(primary_key=True)  
    Bakery_name = models.CharField(max_length=100)  
    Portion_size_per_100g = models.CharField(max_length=100)  
    Calories = models.IntegerField()
    Nutritional_content = models.CharField(max_length=200)  
    class Meta:  
        db_table = "bakery_products"  

class dry_fruits(models.Model):  
    id = models.IntegerField(primary_key=True)  
    dryfruit_name = models.CharField(max_length=100)  
    Portion_size_per_100g = models.CharField(max_length=100)  
    Calories = models.IntegerField()
    Nutritional_content = models.CharField(max_length=200)  
    class Meta:  
        db_table = "dry_fruits" 

class fruits(models.Model):  
    id = models.IntegerField(primary_key=True)  
    fruits_name = models.CharField(max_length=100)  
    Portion_size_per_100g = models.CharField(max_length=100)  
    Calories = models.IntegerField()
    Nutritional_content = models.CharField(max_length=200)  
    class Meta:  
        db_table = "fruits"   
        
class meat_eggs_fishes(models.Model):  
    id = models.IntegerField(primary_key=True)  
    meat_name = models.CharField(max_length=100)  
    Portion_size_per_100g = models.CharField(max_length=100)  
    Calories = models.IntegerField()
    Nutritional_content = models.CharField(max_length=200)  
    class Meta:  
        db_table = "meat_eggs_fishes"   
        
class milk_products(models.Model):  
    id = models.IntegerField(primary_key=True)  
    milkproducts_name = models.CharField(max_length=100)  
    Portion_size_per_100g = models.CharField(max_length=100)  
    Calories = models.IntegerField()
    Nutritional_content = models.CharField(max_length=200)  
    class Meta:  
        db_table = "milk_products"              