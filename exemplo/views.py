from django.shortcuts import render
from django.views.generic import ListView, CreateView
from .models import Cliente

class ClienteList(ListView):
    model = Cliente
    queryset = Cliente.objects.all()
    template_name = 'cliente_list.html'

class ClienteCreate(CreateView):
    model = Cliente
    fields = '__all__'
    success_url = '/clientes/list/'
    template_name = 'cliente_create.html'