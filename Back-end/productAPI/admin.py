from django.contrib import admin
from productAPI.models import Product, Order, OrderItem, Cart, CartItem
# Register your models here.
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'stock', 'is_available')
    search_fields = ('name',)

    ordering = ('name',)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'order_date', 'status')
    search_fields = ('user__username',)
    list_filter = ('status',)
    ordering = ('-order_date',)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = ('order', 'product', 'quantity', 'total_price')  
    search_fields = ('order__id', 'product__name')
    list_filter = ('order', 'product')
    ordering = ('order',)
admin.site.register(Product, ProductAdmin)
admin.site.register(Order, OrderAdmin)  
admin.site.register(OrderItem, OrderItemAdmin)
admin.site.register(Cart)
admin.site.register(CartItem)

