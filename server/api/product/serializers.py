from rest_framework import serializers
from api.product.models.product import Product
# from api.product.models.image import Image


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'
