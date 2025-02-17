# Generated by Django 5.1.3 on 2024-12-12 07:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0034_alter_customer_division_alter_product_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='division',
            field=models.CharField(choices=[('Barisal', 'Barisal'), ('Khulna', 'Khulna'), ('Rajshahi', 'Rajshahi'), ('Rangpur', 'Rangpur'), ('Dhaka', 'Dhaka'), ('Mymensingh', 'Mymensingh'), ('Chittagong', 'Chittagong'), ('Sylhet', 'Sylhet')], max_length=100),
        ),
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.CharField(choices=[('LS', 'Lassi'), ('IC', 'Ice-Creams'), ('GH', 'Ghee'), ('CZ', 'Cheese'), ('MS', 'Milkshake'), ('ML', 'Milk'), ('PN', 'Paneer'), ('CR', 'Curd')], max_length=2),
        ),
    ]
