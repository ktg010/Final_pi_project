from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
import glassy.get_measurables as gm

# Create your views here.
def index(request):
    print("Index Page")
    return render(request, 'glassy\index.html')

def home(request):
    print("Home Page")
    return render(request, 'glassy\home.html')

def analyze(request):
    print("Analyze Page")
    return render(request, r'glassy\analyze.html')

def final(request):
    print("Final Page")
    if gm.M.block == 'A':
        block = "Acrylic"
    elif gm.M.block == 'B':
        block = "Borosilicate"
    elif gm.M.block == 'C':
        block = "optical"
    context = {block: f"{block}"}
    return render(request, r'glassy\final.html', context)