from django.contrib import admin
from . models import Todo, Todolist
# Register your models here.
admin.site.register(Todo)
admin.site.register(Todolist)