from django.urls import path

from . import views

urlpatterns=[
    path('/',views.session_get,name='session_get'),
    path('session_post',views.session_post,name='session_post'),
    path('/m',views.msession_get,name='msession_get'),
    path('/newsess',views.newsess,name='newsess'),
]