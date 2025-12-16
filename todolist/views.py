from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    user = [
    {"name": "Aarav", "age": 15, "address": "Kathmandu", "email": "aarav@gmail.com", "phone": "9800000001", "gender": "Male", "is_active": True},
    {"name": "Sita", "age": 23, "address": "Bhaktapur", "email": "sita@gmail.com", "phone": "9800000002", "gender": "Female", "is_active": True},
    {"name": "Ramesh", "age": 30, "address": "Lalitpur", "email": "ramesh@gmail.com", "phone": "9800000003", "gender": "Male", "is_active": True},
    {"name": "Aarav", "age": 25, "address": "Kathmandu", "email": "aarav25@gmail.com", "phone": "9800000004", "gender": "Male", "is_active": False},
    {"name": "Mina", "age": 28, "address": "Pokhara", "email": "mina@gmail.com", "phone": "9800000005", "gender": "Female", "is_active": True},
    {"name": "Sita", "age": 23, "address": "Bhaktapur", "email": "sita23@gmail.com", "phone": "9800000006", "gender": "Female", "is_active": True},
    {"name": "Kiran", "age": 50, "address": "Butwal", "email": "kiran50@gmail.com", "phone": "9800000007", "gender": "Male", "is_active": True},
    {"name": "Kiran", "age": 35, "address": "Butwal", "email": "kiran35@gmail.com", "phone": "9800000008", "gender": "Male", "is_active": False},
    {"name": "Kiran", "age": 35, "address": "Butwal", "email": "kiran35b@gmail.com", "phone": "9800000009", "gender": "Male", "is_active": True},
    {"name": "Kiran", "age": 65, "address": "Butwal", "email": "kiran65@gmail.com", "phone": "9800000010", "gender": "Male", "is_active": True},
    {"name": "Nisha", "age": 12, "address": "Dharan", "email": "nisha@gmail.com", "phone": "9800000011", "gender": "Female", "is_active": False},
    {"name": "Ramesh", "age": 30, "address": "Lalitpur", "email": "ramesh30@gmail.com", "phone": "9800000012", "gender": "Male", "is_active": True},
    {"name": "Anil", "age": 57, "address": "Biratnagar", "email": "anil@gmail.com", "phone": "9800000013", "gender": "Male", "is_active": True},
    ]
    context = {
        'people': user,
        'title': 'Homepage'
    }
    return render(request, 'home.html', context)


def about_us(request):
    return HttpResponse("<h1> I live in a small village </h1>")

def contact(request):
    return HttpResponse("<h1> contact me thorugh the email </h1>")
