from django.urls import path
from .views import  home,Tasks,contact,create_data,update_data,mark_data ,delete_data#with_slug

urlpatterns = [  
    path('home/', home, name='home' ),
    path('',Tasks , name="task"),
    path('contact/',contact ),
    path('create/',create_data , name="create_data"),
    path('create/<int:id>/',update_data , name="update_data"),
    path('mark/<int:id>/',mark_data , name="mark_data"),
    path('delete/<int:id>/',delete_data , name="delete_data"),
    # path('create/<slug:todo_name>/',with_slug , name="with_slug"),
]
