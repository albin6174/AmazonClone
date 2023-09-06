from django.contrib import admin

# Register your models here.
from store.models import Carts,Products,Category,Offers,Orders
admin.site.register(Category)
admin.site.register(Products)
admin.site.register(Offers)
