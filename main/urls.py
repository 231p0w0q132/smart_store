from django.urls import path

from . import views

app_name='main'

urlpatterns= [
    path('',views.index,name='index'),
    path('ranged_weapon',views.ranged_weapon,name='ranged_weapon'),
    path('combat_weapon',views.combat_weapon,name='combat_weapon'),
    path('etc_weapon',views.etc_weapon,name='etc_weapon'),
    path('all_weapon',views.all_weapon,name='all_weapon'),
    path('shoppingcart/<str:weapone_name>',views.shoppingcart,name='shoppingcart'),
]

