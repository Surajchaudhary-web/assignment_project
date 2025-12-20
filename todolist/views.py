from django.shortcuts import render, get_object_or_404,get_list_or_404, redirect
from django.http import HttpResponse
from . models import Todo, Todolist

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


def Tasks(request):
    tasks = get_list_or_404(Todo)
    count_all = len(tasks)
    context = {
        'tasks':tasks,
        'count_all':count_all,
    }
    return render(request, 'task.html', context)

# def Tasks(request):
#    tasks = Todo.objects.all()
#    count_all = tasks.count()
#    complete = Todo.objects.filter(status = True).count()
#    incomplete = Todo.objects.filter(status = False).count()
#    context = {
#       "tasks" : tasks,
#       "count_all": count_all,
#       "complete_tasks": complete,
#       "incomplete_tasks": incomplete,
#    }
#    print(type(tasks))
#    return render(request,'task.html', context)


def contact(request):
    return HttpResponse("<h1> contact me thorugh the email </h1>")


def create_data(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        Todo.objects.create(title = title, description =description )
        return redirect('task')
    return render(request, 'create_data.html')

def update_data(request, id):
    todo = Todo.objects.get(id = id)
    if request.method == 'POST':
        todo.title = request.POST.get('title')
        todo.description = request.POST.get('description')
        todo.save()
        return redirect('task')
    return render(request, 'update_data.html', {'todo': todo})

# def with_slug(request, todo_name):
#     todo = Todolist.objects.get(slug = todo_name)
#     if request.method == 'POST':
#         todo.title = request.POST.get('title')
#         todo.description = request.POST.get('description')
#         todo.save()
#         return redirect('create_data')
#     return render(request, 'update_data.html', {'todo': todo})

def mark_data(request, id):
    todo = Todo.objects.get(id = id)
    todo.status = not todo.status
    todo.save()
    return redirect('task')


def delete_data(request, id):
    todo = Todo.objects.get(id = id)
    todo.delete()
    return redirect('task')