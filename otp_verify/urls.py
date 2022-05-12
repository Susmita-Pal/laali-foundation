from django.urls import path

from . import views

urlpatterns=[
    path('',views.otp_verify.as_view(),name='otp-verify'),
]