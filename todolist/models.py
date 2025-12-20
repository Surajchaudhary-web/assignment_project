from django.db import models

# Create your models here.
class Todo(models.Model):
   title = models.CharField(max_length=100)
   description = models.TextField()
   status = models.BooleanField(default=True)

   def __str__(self):
      return self.title


class Todolist(models.Model):
   title = models.CharField(max_length=100)
   slug = models.SlugField(max_length=20, unique=True)
   description = models.TextField(default=True)

   def __str__(self):
      return self.title