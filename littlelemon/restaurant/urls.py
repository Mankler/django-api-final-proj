from django.urls import path
from .views import say_hello, index, MenuItemView, SingleMenuItemView
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('hello/', say_hello, name='Hello'),
    path('', index, name='index'),
    path('menu/', MenuItemView.as_view()),
    path('menu/<int:pk>', SingleMenuItemView.as_view()),
    path('api-token-auth/', obtain_auth_token),
]