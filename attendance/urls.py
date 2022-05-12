from django.urls import path

from . import views

urlpatterns=[
    path('',views.attendance,name='attendance'),
    path('/m',views.mattendance,name='mattendance'),
]