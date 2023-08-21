from django.shortcuts import render
from rest_framework import viewsets
from exemplo.models import Cliente
from .serializers import ClienteSerializer
from rest_framework.permissions import IsAuthenticated

class ClienteViewSet(viewsets.ModelViewSet):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer
    permission_classes = [IsAuthenticated]