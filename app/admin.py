from django.contrib import admin
from .models import Brand, Category, Phone, Laptops, Banner, PopularProducts, Television

admin.site.register(Category)
admin.site.register(Phone)
admin.site.register(Laptops)
admin.site.register(PopularProducts)
admin.site.register(Banner)
admin.site.register(Television)
admin.site.register(Brand)
