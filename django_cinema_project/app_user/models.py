from django.db import models


class User(models.Model):
    
    username = models.CharField(max_length=100, unique=True)
    first_name = models.CharField(max_length=120)
    last_name = models.CharField(max_length=120)
    email = models.CharField(max_length=200)
    password = models.CharField(max_length=200)
    phone = models.CharField(max_length=120)
    is_admin = models.BooleanField(default=False)
    
    def __str__(self):
        return f"id         : {self.pk}\n" \
               f"username   : {self.username}\n" \
               f"first_name : {self.first_name}\n" \
               f"last_name  : {self.last_name}\n" \
               f"email      : {self.email}\n" \
               f"password   : {self.password}\n" \
               f"phone      : {self.phone}\n" \
               f"is_admin   : {self.is_admin}\n"    