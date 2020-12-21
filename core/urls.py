from django.urls import path
from .views import *
urlpatterns = [
    path('', List,name="list"),
    path('add/<str:id>/', AddOrder,name="add"),
    path('remove/<str:id>/', RemoveOrder,name="remove"),
    path('cart/', Cart,name="cart"),
]
