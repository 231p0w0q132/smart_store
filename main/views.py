from django.shortcuts import render
from django.http import HttpResponse
def index(request):
    return render(request,"index.html")

def ranged_weapon(request):
    return render(request,"ranged_weapon.html")
