from django.urls import path
from .views import say_hello, index, MenuItemView, SingleMenuItemView

urlpatterns = [
    path('hello/', say_hello, name='Hello'),
    path('', index, name='index'),
    path('menu/', MenuItemView.as_view()),
    path('menu/<int:pk>', SingleMenuItemView.as_view()),
]