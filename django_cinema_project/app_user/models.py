from django.db import models
from django.contrib.auth.models import AbstractBaseUser


class User(AbstractBaseUser):
    username = models.CharField(max_length=100, unique=True)
    first_name = models.CharField(max_length=120)
    last_name = models.CharField(max_length=120)
    email = models.CharField(max_length=150)
    password = models.CharField(max_length=150)
    phone = models.CharField(max_length=120)
    is_admin = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    @classmethod
    def create(cls, username, first_name, last_name, email, password, phone, is_admin):
        return cls(username=username, first_name=first_name, last_name=last_name, 
                   email=email, password=password, phone=phone, is_admin=is_admin)