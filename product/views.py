from django.shortcuts import render
from.serializers import ProductSerializer
from rest_framework import viewsets
from .models import *

# Create your views here.
class ProductViewSet(viewsets.ModelViewSet):
    serializer_class = ProductSerializer
    queryset = productMainModel.objects.all()