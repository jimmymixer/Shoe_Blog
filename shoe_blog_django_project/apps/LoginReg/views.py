from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages
from .models import User
from django.core.urlresolvers import reverse
import bcrypt, re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

def index(request):
    return render(request, 'LoginReg/index.html')

def login(request):
    return render(request, 'LoginReg/login.html')

def r_process(request):  ### validate ###
    data = {
    "name" : request.POST['name'],
    "alias" : request.POST['alias'],
    "email" : request.POST['email'],
    "pass" : request.POST['pass'],
    "c_pass" : request.POST['c_pass'],
    "birth_date": request.POST['birth_date']
    }
    result = User.objects.validate(data)
    if result[0]:
        request.session['user_id'] = result[1].id
        messages.success(request, "Success! ")
        print result[0]
        return redirect("/")
    else:
        for err in result[1]:
            print result[1]
            messages.error(request, err)
        return redirect("/")

def l_process(request): ### success ###
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['pass']
        if not User.objects.filter(email=email):
            context = {
                'error': 'Email not found'
            }
            return render(request, 'LoginReg/index.html', context)
        user = User.objects.filter(email=email)
        if bcrypt.hashpw(str(password), str(user[0].password)) == user[0].password:
            request.session['user_id'] = user[0].id
            #this put user IN session
        else:
            context = {
                'pass': 'Password not valid'
            }
            return render(request, 'LoginReg/index.html', context)
        # return redirect(reverse('plans:page'))
        return redirect(reverse('quotes:qindex')) #### change this to the new site quotes

def logout(request):
    request.session.clear()
    return redirect("/")
