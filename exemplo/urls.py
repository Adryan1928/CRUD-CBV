from django.urls import path
from . import views

app_name = 'exemplo'

urlpatterns = [
    path('list/', view=views.ClienteList.as_view(), name='list'),
    path('create/', view=views.ClienteCreate.as_view(), name='create')
]