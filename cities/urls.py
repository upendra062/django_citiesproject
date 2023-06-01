from django.urls import path
from . import views 


urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('cities/', views.cities, name='cities'),
    path('cities/details/<int:id>/', views.details, name='details'),
    path('cities/last/<int:id>/', views.last, name='last'),
    path('template/', views.template, name='template'),
    path('template2/', views.template2, name='template2'),
    path('cities/newdynamic/', views.newdynamic, name='newdynamic'),
    path('users/', views.users, name='users'),
    path('users1/', views.users1, name='users1'),
]
