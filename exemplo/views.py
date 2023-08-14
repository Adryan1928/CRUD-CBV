from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, DetailView, DeleteView
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

class ClienteUpdate(UpdateView):
    model = Cliente
    fields = '__all__'
    success_url = '/clientes/list/'
    template_name = 'cliente_update.html'

class ClienteDetail(DetailView):
    model = Cliente
    queryset = Cliente.objects.all()
    template_name = 'cliente_detail.html'

class ClienteDelete(DeleteView):
    model = Cliente
    queryset = Cliente.objects.all()
    success_url = '/clientes/list/'
    template_name = 'cliente_delete.html'