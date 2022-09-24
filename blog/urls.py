
from django.urls import path, include
from . import views


urlpatterns = [
    path('',views.index),
    path('http://samsblogapp.herokuapp.com/createblog/',views.createblog),
    path('http://samsblogapp.herokuapp.com/myblog/',views.myblog)
]
