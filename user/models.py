from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class PostUser(AbstractUser):
    city= models.CharField(max_length = 100,null = True)
    phone = models.CharField(max_length = 12, null = True)
