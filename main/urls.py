from django.urls import path

from . import views

app_name='main'

urlpatterns= [
    path('',views.index,name='index'),
    path('ranged_weapon',views.ranged_weapon,name='ranged_weapon'),
]

