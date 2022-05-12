from django.urls import path

from . import views

urlpatterns=[
    path('',views.mdetails,name='details'),
    path('/m',views.mdetails,name='mdetails'),
    path('/ad',views.addetails,name='mdetails'),
]