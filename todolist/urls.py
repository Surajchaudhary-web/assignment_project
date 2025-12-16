from django.urls import path
from .views import home,about_us,contact

urlpatterns = [   
    path('home/', home, name='home' ),
    path('aboutus/',about_us ),
    path('contact/',contact ),
]
