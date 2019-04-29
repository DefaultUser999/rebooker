# textbook/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('signup/', views.SignUp.as_view(), name='signup'),
    path('sell/', views.sell, name='sell')
    # path('buy/', views.buy, name='buy'),
]