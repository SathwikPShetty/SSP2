from django.contrib import admin
from django.urls import path
from team import views

urlpatterns = [
    path('',views.index,name='home'),
    # path("about",views.about,name='about'),
    path('team',views.team,name='team'),
    # path("contact",views.contact,name='contact'),
]