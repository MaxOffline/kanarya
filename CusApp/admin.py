from django.contrib import admin
from .models import newcustomer, Item, Cart

# Register your models here.
admin.site.register(newcustomer)
admin.site.register(Item)
admin.site.register(Cart)
