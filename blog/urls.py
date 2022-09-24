
from django.urls import path, include
from . import views


urlpatterns = [
    path('',views.index),
    path('createblog/',views.createblog),
    path('myblog/',views.myblog)
]
