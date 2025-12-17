from django.urls import path
from .views import home,Tasks,contact

urlpatterns = [   
    path('home/', home, name='home' ),
    path('todolist/',Tasks ),
    path('contact/',contact ),
]
