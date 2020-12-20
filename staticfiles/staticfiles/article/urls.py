from django.contrib import admin
from django.urls import path
from article import views

app_name="article"

urlpatterns = [
    path('dashboard/',views.dashboard,name="articles/dashboard"),
    path('addarticle/',views.addarticle,name="addarticle"),
    path('article/<int:id>',views.detail,name="detail"),
]
