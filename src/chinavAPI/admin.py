from django.contrib import admin
from .models import ProductsModels

# Register your models here.

class Product(admin.ModelAdmin):
    pass

admin.site.register(ProductsModels,Product)
