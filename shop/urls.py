from django.urls import path
from .views import *

urlpatterns = [
    path('', index.as_view(),name='index'),
    path('login', Login.as_view(),name='login'),
    path('register', Register.as_view(),name='register'),
    path('logout', logout,name='logout'),
]