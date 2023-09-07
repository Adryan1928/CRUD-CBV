from django.urls import path, include
from . import views

urlpatterns = [
    path('', include('django.contrib.auth.urls')),
    path('register/', view=views.RegisterUserView, name='register'),
    path('detail_user/<int:pk>', view=views.userDetailView.as_view(), name='detail')
]