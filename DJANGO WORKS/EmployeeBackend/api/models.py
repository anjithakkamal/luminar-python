from unicodedata import name
from django.db import models

# Create your models here.

# name,department,place,salary,profile

class Employee(models.Model):

    name=models.CharField(max_length=200)

    department=models.CharField(max_length=200)

    place=models.CharField(max_length=200)

    salary=models.PositiveIntegerField()

    email=models.EmailField()

    profile=models.ImageField(upload_to="images",null=True,blank=True)

    def __str__(self):
        
        return self.name
    
