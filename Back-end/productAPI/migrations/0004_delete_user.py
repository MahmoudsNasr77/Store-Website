# Generated by Django 5.1.7 on 2025-04-14 19:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('productAPI', '0003_product_slug'),
    ]

    operations = [
        migrations.DeleteModel(
            name='User',
        ),
    ]
