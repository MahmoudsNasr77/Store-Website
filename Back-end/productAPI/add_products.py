from django.core.management.base import BaseCommand
from .models import Product

class Command(BaseCommand):
    help = 'Adds products to the database'

    def handle(self, *args, **kwargs):
        products = [
            {
                "image": "https://example.com/placeholder.jpg",
                "name": "Dell XPS 13",
                "description": "High-performance laptop with sleek design.",
                "price": 1199.99,
                "stock": 50
            },
            {
                "image": "https://example.com/placeholder.jpg",
                "name": "MacBook Pro 16",
                "description": "Premium laptop for professionals with advanced features.",
                "price": 2399.99,
                "stock": 30
            },
            {
                "image": "https://example.com/placeholder.jpg",
                "name": "HP Spectre x360",
                "description": "Convertible 2-in-1 laptop with elegant design and powerful specs.",
                "price": 1499.99,
                "stock": 40
            },
            {
                "image": "https://example.com/placeholder.jpg",
                "name": "Lenovo ThinkPad X1",
                "description": "Business laptop with powerful specs and great durability.",
                "price": 1999.99,
                "stock": 20
            },
            {
                "image": "https://example.com/placeholder.jpg",
                "name": "Asus ROG Strix",
                "description": "Gaming laptop with RTX graphics for superior performance.",
                "price": 1699.99,
                "stock": 60
            },
            {
                "image": "https://example.com/placeholder.jpg",
                "name": "Microsoft Surface Laptop 4",
                "description": "High-end laptop for creators with stunning display and performance.",
                "price": 1499.99,
                "stock": 80
            },
            {
                "image": "https://example.com/placeholder.jpg",
                "name": "Acer Predator Helios 300",
                "description": "Gaming laptop with powerful cooling system and great performance.",
                "price": 1299.99,
                "stock": 100
            },
            {
                "image": "https://example.com/placeholder.jpg",
                "name": "Alienware m15",
                "description": "Gaming laptop with immersive display and premium features.",
                "price": 1799.99,
                "stock": 75
            },
            {
                "image": "https://example.com/placeholder.jpg",
                "name": "Razer Blade 15",
                "description": "Thin and light gaming laptop with excellent build quality.",
                "price": 2199.99,
                "stock": 90
            },
            {
                "image": "https://example.com/placeholder.jpg",
                "name": "Samsung Galaxy Book Pro",
                "description": "Thin, powerful laptop with AMOLED screen and ultra-fast performance.",
                "price": 1599.99,
                "stock": 60
            }
        ]

        for product in products:
            Product.objects.create(
                image=product['image'],
                name=product['name'],
                description=product['description'],
                price=product['price'],
                stock=product['stock']
            )

        self.stdout.write(self.style.SUCCESS('Successfully added products to the database!'))
