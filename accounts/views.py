from django.shortcuts import render, redirect
# from django.urls import reverse
# from .models import UserModel
from django.contrib.auth.models import User
from counter.models import CounterModel
from .forms import UserForm
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.http import JsonResponse
import json

# Create your views here.
def home(request):
    return render(request, 'accounts/home.html')

def counting(request):
    param = request.GET['counter']
    is_init = request.GET['init']
    print(is_init)
    counter = CounterModel.objects.all()
    if counter.count() > 0:
        data = counter[0]
        if not eval(is_init):
            data.press_count +=1
            data.save()
        number = data.press_count
    else:
        number = 0
        CounterModel.objects.create(press_count=number)
    return JsonResponse({'count': number})

def add(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            is_exists = User.objects.filter(username=form.cleaned_data['username']).exists()
            print(is_exists)
            if is_exists:
                form = UserForm()
                return render(request, 'accounts/register.html', {'form': form, 'is_exists': is_exists})
            else:
                user = User.objects.create_user(username=form.cleaned_data['username'], password=form.cleaned_data['password'])
                # user.save()
                return redirect('login')
            
    else:
        form = UserForm()
    return render(request, 'accounts/register.html', {'form': form})

def login_request(request):
    if request.method == 'POST':
        print(request.POST, 'jhgjhgjh')
        form = AuthenticationForm(request, data=request.POST)
        # form = UserForm(request.POST)
        print(form)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            print(username)
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                print('login with '+ username)
                print(user)
                return redirect('home')
    form = AuthenticationForm()
    return render(request, 'accounts/login.html', {'form': form})

# def login(request):
#     if request.method == 'POST':
#         form = UserForm(request.POST)
#         if form.is_valid():
#             found = UserModel.objects.filter(username=form.cleaned_data['username']).filter(password=form.cleaned_data['password'])
#             print(found)
#             if found.count() > 0:
#                 data = found[0]
#                 data.is_authenticated = True
#                 data.save()
#                 print(data.id)
#                 return HttpResponseRedirect('/')
#                 # return redirect(reverse('home', kwargs={'is_authenticated': True, 'id':data.id}))
#                 # return render(request, 'accounts/home.html', {'is_authenticated': True, 'id':data.id})
#     else:
#         form = UserForm()
#     return render(request, 'accounts/login.html', {'form': form})

def logout_request(request):
    logout(request)
    return redirect('home')

# def logout(request, id):
#     user = UserModel.objects.get(pk=id)
#     user.is_authenticated = False
#     user.save()
#     form = UserForm()
#     return render(request, 'accounts/login.html', {'form': form})
    

def update(request):
    pass

def delete(request):    
    pass
