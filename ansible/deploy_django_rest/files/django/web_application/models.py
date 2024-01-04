from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.urls import reverse

class Employee(models.Model):
    first_name = models.CharField(max_length=100)
    second_name = models.CharField(max_length=100)
    department = models.CharField(max_length=100)
    email = models.EmailField()
    date = models.DateField()
    level = models.IntegerField(validators =[MinValueValidator(1), MaxValueValidator(5)])
       
    def __str__(self) -> str:
        return f"{self.first_name} {self.second_name} - {self.department}"
