
from django.urls import path
from depapp.views import index

urlpatterns = [
    path('',index),
]
