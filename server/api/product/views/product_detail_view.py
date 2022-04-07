from api.product.models.product import Product
from rest_framework import generics
from api.product.serializers import ProductSerializer


class ProductDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
