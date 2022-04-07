from api.product.models.product import Product
from rest_framework import generics
from api.product.serializers import ProductSerializer
from django.db.models import Q


class ProductSearchListView(generics.ListAPIView):
    model = Product
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    paginate_by = 10

    def get_queryset(self):
        query_set = super().get_queryset()

        serch_word = self.request.query_params.get('searchWord', None)
        if serch_word:
            query_set = query_set.filter(
                Q(name__icontains=serch_word) | Q(explanation__icontains=serch_word))

        product_category = self.request.query_params.get('lergeCategoryCode', None)
        if product_category:
            query_set = query_set.filter(product_category=product_category)

        product_subcategory = self.request.query_params.get('mediumCategoryCode', None)
        if product_subcategory:
            query_set = query_set.filter(product_subcategory=product_subcategory)

        return query_set
