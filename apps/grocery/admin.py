from django.contrib import admin
from .models import GroceryList, GroceryItems
# Register your models here.
admin.site.register(GroceryList)
admin.site.register(GroceryItems)
