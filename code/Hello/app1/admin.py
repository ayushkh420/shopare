from django.contrib import admin
from app1.models import ProductGrocery
from app1.models import Contact
from app1.models import Grocery


class AdminProduct(admin.ModelAdmin):
    list_display = ['product_name', 'price', 'grocery']


admin.site.register(ProductGrocery, AdminProduct)
admin.site.register(Contact)
admin.site.register(Grocery)


