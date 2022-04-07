from django.urls import path
from api.product.views.product_search_view import ProductSearchListView
from api.product.views.product_detail_view import ProductDetailView

app_name = 'product'

urlpatterns = [
    path('search/', ProductSearchListView.as_view(), name='product_search'),
    path('detail/<str:pk>', ProductDetailView.as_view(), name='product_detail'),
]
