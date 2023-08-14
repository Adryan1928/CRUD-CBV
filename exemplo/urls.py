from django.urls import path
from . import views

app_name = 'exemplo'

urlpatterns = [
    path('list/', view=views.ClienteList.as_view(), name='list'),
    path('create/', view=views.ClienteCreate.as_view(), name='create'),
    path('update/<int:pk>/', view=views.ClienteUpdate.as_view(), name='update'),
    path('detail/<int:pk>/', view=views.ClienteDetail.as_view(), name='detail'),
    path('delete/<int:pk>/', view=views.ClienteDelete.as_view(), name='delete')
]