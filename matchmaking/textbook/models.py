from django.db import models

# Create your models here.

class User(models.Model):
    # ID - Primary key
    # each user must have a unique email
    email = models.EmailField(max_length=254)
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)

class item:
    # ID - Primary Key
    # maybe have the textbook name plus and
    # interger to allow for multiple books of the same name

    name = models.CharField(max_length=100)
    author = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    # used to check if textbook is sold or not
    # true == sold
    status_sold = models.BooleanField(default=False)
    # foreign key
    # references the user model class
    seller = models.ForeignKey(User, on_delete=models.CASCADE)
