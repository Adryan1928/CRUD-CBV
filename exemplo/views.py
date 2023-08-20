from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, DetailView, DeleteView
from .models import Cliente
from django.contrib.auth.mixins import LoginRequiredMixin

class ClienteList(LoginRequiredMixin, ListView):
    model = Cliente
    queryset = Cliente.objects.all()
    template_name = 'cliente_list.html'

class ClienteCreate(LoginRequiredMixin, CreateView):
    model = Cliente
    fields = '__all__'
    success_url = '/clientes/list/'
    template_name = 'cliente_create.html'

class ClienteUpdate(LoginRequiredMixin, UpdateView):
    model = Cliente
    fields = '__all__'
    success_url = '/clientes/list/'
    template_name = 'cliente_update.html'

class ClienteDetail(LoginRequiredMixin, DetailView):
    model = Cliente
    queryset = Cliente.objects.all()
    template_name = 'cliente_detail.html'

class ClienteDelete(LoginRequiredMixin, DeleteView):
    model = Cliente
    queryset = Cliente.objects.all()
    success_url = '/clientes/list/'
    template_name = 'cliente_delete.html'