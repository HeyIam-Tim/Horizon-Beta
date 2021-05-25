from django.contrib import admin
from .models import *

class ProductAdmin(admin.ModelAdmin):
    list_display = ('unique_number', 'name', 'qauntity')


admin.site.register(MainStorage)
admin.site.register(Shop)
admin.site.register(Product, ProductAdmin)



