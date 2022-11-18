from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(productMainModel)
admin.site.register(ProductColourModel)
admin.site.register(ProductImageModel)