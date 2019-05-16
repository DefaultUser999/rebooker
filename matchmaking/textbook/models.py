from django.db import models
from django.contrib.auth import get_user_model
from django.contrib.auth.models import AbstractUser
from django.utils.timezone import now
from django.urls import reverse

class CustomUser(AbstractUser):
    # add additional fields in here

    def __str__(self):
        return self.email

class Item(models.Model):
    seller = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
        related_name='user_selling_item'
    )
    sell_date = models.DateTimeField(auto_now_add=True)
    # buy_date
    name = models.CharField(max_length=100)
    author = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    status_sold = models.BooleanField(default=False) # used to check if textbook is sold or not : true == sold
    buyer = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
        related_name='user_buying_item',
        # primary_key=False
        null=True
    )
    # title = models.CharField(max_length=100)
    # description = models.TextField(blank=True, null=True)
    # featured    = models.BooleanField(default=False) # null=True, default=True
    def print_info(self):
        return "seller: " + self.seller + "Buyer: " + self.buyer

class Category(models.Model):
    name = models.CharField(max_length=150, db_index=True)
    slug = models.SlugField(max_length=150, unique=True ,db_index=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('name', )
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('textbook:product_list_by_category', args=[self.slug])


class Product(models.Model):
    category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE)
    name = models.CharField(max_length=100, db_index=True)
    slug = models.SlugField(max_length=100, db_index=True)
    condition = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    available = models.BooleanField(default=True)
    stock = models.PositiveIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    image = models.ImageField(upload_to='products/%Y/%m/%d', blank=True)

    class Meta:
        ordering = ('name', )
        index_together = (('id', 'slug'),)

    def __str__(self):
        return self.name
        
    def get_absolute_url(self):
        return reverse('textbook:product_detail', args=[self.id, self.slug])

