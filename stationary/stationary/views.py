from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
# Create your views here.

def index(request):
    return render(request, "index.html")

def products(request):
    return render(request, "products.html")

def case(request):
    return render(request, "products_case.html")

def note(request):
    return render(request, "products_note.html")

def pen(request):
    return render(request, "products_pen.html")

def pencil(request):
    return render(request, "products_pencil.html")