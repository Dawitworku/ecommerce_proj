from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages
from .models import *
import bcrypt

# Create your views here.


def index(request):
    return render(request, 'index.html')


def register(request):
    if request.method == 'POST':
        # print(request.POST)

        errors = User.objects.validator(request.POST)
        if errors:
            for key, value in errors.items():
                messages.error(request, value)
        else:
            hashed_pw = bcrypt.hashpw(
                request.POST['password'].encode(), bcrypt.gensalt()).decode()

            this_user = User.objects.create(
                first_name=request.POST['first_name'],
                last_name=request.POST['last_name'],
                email=request.POST['email'],
                birthday=request.POST['birthday'],
                password=hashed_pw,
            )
            request.session['user_id'] = this_user.id
            messages.success(request, "Successfully Created an Account. Please Login Using Your Email")
            return redirect('/')
    return redirect('/')


def email_check(request):
    #print(request.POST['email'])

    message = "Email is available"
    errors = User.objects.email_validator(request.POST['email'])
    if errors:
        message = "Email is in use"

    context = {
        'message': message
    }
        # for key, value in errors.items():
        #messages.error(request, value)
        # email_dup = User.objects.filter(email= request.POST['email'])

    # return render(request, 'email_val_ajax.html', context) 
    #Using Http response instead of rendering and using partial html for the error message
    return HttpResponse(f'{message}')


def login(request):
    if request.method == "POST":
        this_user = User.objects.filter(email=request.POST['email'])
        if len(this_user) == 1:  # Filter return a list on objects that exist in our DB
            this_user = this_user[0]
            if bcrypt.checkpw(request.POST['password'].encode(), this_user.password.encode()):
                # storing the user identity in our sessions here
                request.session['user_id'] = this_user.id
                return redirect('/welcome')

        messages.error(request, "Email or Password not found")

    return redirect('/')


def welcome_page(request):

    if 'user_id' not in request.session:  # making sure only logged in users are using the app
        messages.error(
            request, "You need to register or log in if you already have an account!")
        return redirect('/')
    else:
        context = {
            'user': User.objects.get(id=request.session['user_id'])
        }
        messages.success(request, "Successfully Logged in!")
    return render(request, 'welcome_page.html', context)


def logout(request):
    request.session.flush()
    return redirect('/')
