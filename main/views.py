from django.shortcuts import render
from django.http import HttpResponse
from .models import items

def index(request):
    return render(request,"index.html")

def ranged_weapon(request):
    weapone=items.objects.all()
    context={"items":weapone}
    return render(request,"weapon_list.html",context)
