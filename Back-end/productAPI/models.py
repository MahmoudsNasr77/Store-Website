import uuid
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models import Sum
from django.utils.translation import gettext_lazy as _
from django.utils.text import slugify
from accounts.models import CustomUser
from django.conf import settings



class Product(models.Model):
    ELECTRONICS = 'electronics'
    FASHION = 'fashion'
    HOME = 'home'
    
    CATEGORY_CHOICES = [
        (ELECTRONICS, _('Electronics')),
        (FASHION, _('Fashion')),
        (HOME, _('Home')),
    ]
    name = models.CharField(max_length=100, verbose_name=_("Product Name"))
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.IntegerField()
    image= models.ImageField(upload_to='images/', blank=True, null=True)
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES, default=ELECTRONICS)

    slug = models.SlugField(unique=True, blank=True, null=True)
 
    @property
    def is_available(self):
        return self.stock > 0
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)
    def __str__(self):
        return self.name
class Order(models.Model):
    class status(models.TextChoices):
        PENDING = 'Pending', 'Pending'
        CANCELLED = 'Cancelled', 'Cancelled'
        DELIVERED = 'Delivered', 'Delivered'
    id=models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    product = models.ManyToManyField(through='OrderItem', to=Product)
    order_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, default='Pending')
    def __str__(self):
        return f"Order {self.id} by {self.user.username}"
class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    @property
    def total_price(self):
        return self.product.price * self.quantity
    
    @property
    def product_quantity(self):
        ordered_quantity = self.orderitem_set.aggregate(Sum('quantity'))['quantity__sum'] or 0
        return self.stock - ordered_quantity
    def __str__(self):
        return f"{self.quantity} of {self.product.name} in Order {self.order.id}"
class Cart(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="cart")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Cart of {self.user.username}"

class CartItem(models.Model):
    cart = models.ForeignKey(Cart, related_name="items", on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    added_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.quantity} x {self.product.name}"

    @property
    def total_price(self):
        return self.quantity * self.product.price