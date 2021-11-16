from django.contrib import admin
from django.urls import path,include
from portfoliotracker import views as s
urlpatterns = [

    path('',s.index),
    path('test/',s.test)

]