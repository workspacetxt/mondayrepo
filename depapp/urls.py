
from django.urls import path
from depapp.views import home

urlpatterns = [
    path('',home,name="home"),
]
