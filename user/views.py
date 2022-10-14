from django.shortcuts import render, redirect
from .models import UserModel
from django.contrib import auth

# Create your views here.


def login_view(request):

    if request.method == 'GET':
        return render(request, 'login.html')
    
    elif request.method == 'POST':
        user_author = request.POST.get('username','')
        user_password = request.POST.get('password','')

        me = UserModel.objects.get(username=user_author)

        if user_password == me.password:
            auth.login(request, me)
            return redirect('/')
        else:
            return redirect('/login')


        

def sign_up(request):
    if request.method == 'POST':
        username = request.POST.get('username','')
        password = request.POST.get('password','')
        phonenum = request.POST.get('phone','')
        address = request.POST.get('address','')

        UserModel.objects.create_user(username=username, password=password, phonenum=phonenum, address=address)


        return redirect('/login')

    elif request.method == 'GET':
        return render(request, 'signup.html')


def homepage(request):
    if request.method == 'GET':
        user = request.user.is_authenticated
        if user:
            return render(request, 'home.html')
        else: 
            return redirect('/login')