from django.contrib.auth.models import AbstractUser
from django.db import models
# Create your models here.
class Usuario(AbstractUser):
   first_name = models.CharField(max_length=50, default="") 
   last_name = models.CharField(max_length=50, default="")
   username = models.CharField(max_length=20, unique=True)
   email = models.EmailField(max_length=50, default = "")
   age = models.PositiveIntegerField(default=18)
   photo = models.ImageField(default='images/deafualt.png')
   role = models.CharField(max_length=10, default="")