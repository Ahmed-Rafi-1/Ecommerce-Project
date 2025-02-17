# Generated by Django 5.1.3 on 2024-12-12 09:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0044_alter_customer_division_alter_product_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='division',
            field=models.CharField(choices=[('Chittagong', 'Chittagong'), ('Mymensingh', 'Mymensingh'), ('Khulna', 'Khulna'), ('Dhaka', 'Dhaka'), ('Rajshahi', 'Rajshahi'), ('Rangpur', 'Rangpur'), ('Sylhet', 'Sylhet'), ('Barisal', 'Barisal')], max_length=100),
        ),
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.CharField(choices=[('IC', 'Ice-Creams'), ('CR', 'Curd'), ('PN', 'Paneer'), ('GH', 'Ghee'), ('ML', 'Milk'), ('MS', 'Milkshake'), ('LS', 'Lassi'), ('CZ', 'Cheese')], max_length=2),
        ),
    ]
