# Create your views here.
from __future__ import unicode_literals
from django.shortcuts import render, HttpResponse, redirect
import re

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')


def index(request):
    # context={
    #     'user': User.objects.all()
    # }
    return render (request, 'loginreg/index.html')

# def new(request):
#     return render (request, 'semirestful_users/new.html')

# def add(request):
#     first_name= request.POST['first_name']
#     last_name= request.POST['last_name']
#     email= request.POST['email']
#     User.objects.create(first_name= first_name, last_name=last_name, email=email)
#     return redirect ('/')