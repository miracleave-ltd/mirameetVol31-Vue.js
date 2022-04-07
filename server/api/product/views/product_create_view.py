from api.product.models.image import Image
from api.product.models.product import Product
from django.urls import reverse_lazy
from django.views.generic import CreateView


class CreateProductView(CreateView):
    model = Product
    template_name = 'product/product_create.html'
    success_url = reverse_lazy('product:product_create')
