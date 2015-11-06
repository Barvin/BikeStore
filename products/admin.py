from django.contrib import admin
from models import Product

# Register your models here

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', )
    search_fields = ['name']

# so that it shows up in the admin console
admin.site.register(Product, ProductAdmin)
