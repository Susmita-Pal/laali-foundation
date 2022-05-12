from django.urls import path

from . import views

urlpatterns=[
    path('',views.assignments,name='assignments'),
    path('/score/',views.score,name='score'),
]