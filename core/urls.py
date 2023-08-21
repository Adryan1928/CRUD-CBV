from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from api.views import ClienteViewSet
from django.views.generic import TemplateView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

router = routers.DefaultRouter()
router.register('clientes', ClienteViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', view=TemplateView.as_view(template_name='home.html'), name='home'),
    path('clientes/', include('exemplo.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('token/', TokenObtainPairView.as_view()),
    path('token/refresh/', TokenRefreshView.as_view())
] + [path('api/', include(router.urls))]
