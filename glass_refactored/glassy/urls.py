from django.urls import path
from . import views

urlpatterns = [

    path('index/', views.index),
    path('home/', views.home),
    path('analyze/', views.analyze),
    path('final/', views.final),

]