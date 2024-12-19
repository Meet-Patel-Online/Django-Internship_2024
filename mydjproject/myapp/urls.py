from django.urls import path    
from . import views

urlpatterns = [
    path('',views.home),
    path('home',views.home),
    path('login',views.login),
    path('login',views.addstudent),
    path('demo',views.displayStudent),
    path('delete-student/<int:id>',views.deletestudent,name='delete-student'),
]
