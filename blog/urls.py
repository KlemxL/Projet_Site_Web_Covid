# -*- coding: utf-8 -*-

from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='blog-home'),
    path('demandes/', views.demandes, name='blog-demandes'),
     path('collectivite/', views.collectivite, name='blog-collectivite'),
    #path('demandeurs/', views.demandeurs, name='blog-demandeurs'),
]