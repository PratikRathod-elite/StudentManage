from django.db import models

# Create your models here.
class Students(models.Model):
    name = models.CharField(max_length=100)
    roll = models.IntegerField()
    Gender = models.CharField(max_length=10)
    division = models.CharField(max_length=10)
    year = models.CharField(max_length=10)
    branch = models.CharField(max_length=10)
    dob = models.DateField()
    prn = models.CharField(max_length=15)
    email = models.EmailField()
    contact = models.CharField(max_length=10)
    address = models.TextField()
