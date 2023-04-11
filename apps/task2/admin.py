from django.contrib import admin
from .models import Review, Service, Product
# Register your models here.

admin.site.register(Service)
admin.site.register(Product)
admin.site.register(Review)
