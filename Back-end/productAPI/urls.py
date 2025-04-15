app_name="productAPI"
from django.urls import path
from .views import ProductList,ProductDetail,OrderList,OrderDetail,OrderItemList,OrderItemDetail,ProductViewSet,ProductAdd,AddItemToCart
from django.urls import path, include

urlpatterns = [
  path('products/', ProductList.as_view(), name='product-list'),
  path('products/<str:slug>/', ProductDetail.as_view(), name='product-detail'),
    path('orders/', OrderList.as_view(), name='order-list'),
    path('orders/<uuid:order_id>/', OrderDetail.as_view(), name='order-detail'),
    path('orderitems/', OrderItemList.as_view(), name='orderitem-list'),
    path('orderitems/<int:pk>/', OrderItemDetail.as_view(), name='orderitem-detail'),
    path('add_product',ProductAdd.as_view(),name="add_product"),

    path('product_search',ProductViewSet.as_view({'get':'list'}),name="ProductSearch"),
    path('cart/add_item/', AddItemToCart.as_view(), name='add_item_to_cart'),

    

]   