from django.urls import path
from .views import say_hello, index

urlpatterns = [
    path('hello/', say_hello, name='Hello'),
    path('', index, name='index')
]