from typing import Any
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect
from django.views.generic import CreateView
from django.contrib.auth.models import User
from django.urls import reverse_lazy

# class RegisterUserView(CreateView):
#     model = User
#     fields = ('username', 'password')
#     template_name = 'registration/register.html'
#     success_url = reverse_lazy('exemplo:list')

def RegisterUserView(request):
    if request.method == 'GET':
        return render(request, 'registration/register.html')
    else:
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = User.objects.filter(username = username).first()

        if user:
            return render(request, 'registration/register.html', {'msg' : 'Já existe um usuário com esse username'})

        user = User.objects.create_user(username=username, password=password)
        user.save()

        return redirect('/accounts/login/')