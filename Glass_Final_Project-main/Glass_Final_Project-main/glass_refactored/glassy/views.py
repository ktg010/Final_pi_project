from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from glassy.mainfile import func
import os

# Create your views here.
def index(request):
    print("Index Page")
    return render(request, 'glassy/index.html')

def home(request):
    print("Home Page")
    return render(request, 'glassy/home.html')

def analyze(request):
    print("Analyze Page")
    return render(request, r'glassy/analyze.html')


#def final(request):
#    print("Final Page")
#    return render(request, r'glassy/final.html')

def run(request):
    result = func()
    context = {'block': result}
    return render(request, r'glassy/final.html', context)
