from django.shortcuts import render

# Create your views here.
import json
from django.contrib.auth.models import User
from django.views import View
from django.http import HttpResponse

class Registration(View):

    def post(self,request,*args,**kwargs):

        request_data=json.loads(request.body)

        print(request_data)

        email=request_data['email']
        username=request_data['username']
        password=request_data['password']

        user_obj=User.objects.create(email=email,username=username,password=password)

        print(user_obj)
        # user_obj.save()

        return HttpResponse("hi")


# class Note(View):
#
#     def get(self,request,*args,**kwargs):
#
#         pass
#
#     def post(self,request,*args,**kwargs):
#
#         pass