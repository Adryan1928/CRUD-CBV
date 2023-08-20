from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from api.views import ClienteViewSet
from django.views.generic import TemplateView

router = routers.DefaultRouter()
router.register('clientes', ClienteViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', view=TemplateView.as_view(template_name='home.html'), name='home'),
    path('clientes/', include('exemplo.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
] + [path('api/', include(router.urls))]
