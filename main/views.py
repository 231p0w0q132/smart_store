from django.shortcuts import render
from django.http import HttpResponse
from .models import items

def index(request):
    return render(request,"index.html")

def ranged_weapon(request):
    weapone=items.objects.filter(typ='원거리')
    context={"items":weapone}
    return render(request,"weapon_list.html",context)

def combat_weapon(request):
    weapone=items.objects.filter(typ='근접')
    context={"items":weapone}
    return render(request,"weapon_list.html",context)
    
def etc_weapon(request):
    weapone=items.objects.filter(typ='기타')
    context={"items":weapone}
    return render(request,"weapon_list.html",context)
    
def all_weapon(request):
    weapone=items.objects.all()
    context={"items":weapone}
    return render(request,"weapon_list.html",context)

def
