import random

from django.shortcuts import render
from rest_framework.views import APIView
from django.conf import settings
from twilio.rest import Client
from django.http import JsonResponse


# Create your views here.
def generateOTP():
    return random.randrange(100000, 999999)


class otp_verify(APIView):
    def post(self,request):
        account_sid = settings.SENDSMS_ACCOUNT_SID
        auth_token = settings.SENDSMS_AUTH_TOKEN
        number = "+917260983222"
        client = Client(account_sid, auth_token)
        otp = generateOTP()
        body = "Your OTP is" + str(otp)
        message = client.messages.create(from_=settings.SENDSMS_FROM_NUMBER, to=number, body=body)
        if message.sid:
            print("Sent successful")
            return JsonResponse({"success": True})
        else:
            print("Unsuccessful")
            return JsonResponse({"success": False})
