from django.contrib import admin
from .models.product import Product
from .models.image import Image


admin.site.register(Product)
admin.site.register(Image)

