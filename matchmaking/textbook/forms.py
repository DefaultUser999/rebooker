# textbook/forms.py
from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser, Item

from django.forms import ModelForm

class CustomUserCreationForm(UserCreationForm):

    class Meta(UserCreationForm):
        model = CustomUser
        fields = ('username', 'email')

class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = CustomUser
        fields = ('username', 'email')

class SellItemForm(ModelForm):
    class Meta:
        model = Item
        fields = [
            'name', # title
            'author',
            'price'
            # title
        ]
        widget = {
            'name': forms.TextInput( attrs={"placeholder": "Your title" } ),
            }
    # name = forms.CharField(label='name', widget=forms.TextInput( attrs={"placeholder": "Your title" }))
    # def is_valid():

class BuyItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = [
            'name',
            'author',
            'price'
        ]
        widget = {

        }
