from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return HttpResponse("<h1> Hello world we are living the earth </h1>")

def about_us(request):
    return HttpResponse("<h1> I live in a small village </h1>")

def contact(request):
    return HttpResponse("<h1> contact me thorugh the email </h1>")
