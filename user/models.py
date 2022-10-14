from tkinter import Y
from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class UserModel(AbstractUser):
    class Meta:
        db_table="my_user"

    phonenum = models.CharField(max_length=256)
    address = models.CharField(max_length=256)