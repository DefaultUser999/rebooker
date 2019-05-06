from django.db import models
from django.contrib.auth import get_user_model
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    # add additional fields in here

    def __str__(self):
        return self.email

class Item(models.Model):
    seller = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE
    )
    sell_date = models.DateTimeField( auto_now=True, auto_now_add=True)
    # buy_date
    name = models.CharField(max_length=100)
    author = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    status_sold = models.BooleanField(default=False) # used to check if textbook is sold or not : true == sold
    # buyer = models.ForeignKey(
    #     get_user_model(),
    #     on_delete=models.CASCADE
    # )
    # title = models.CharField(max_length=100)
    # description = models.TextField(blank=True, null=True)
    # featured    = models.BooleanField(default=False) # null=True, default=True