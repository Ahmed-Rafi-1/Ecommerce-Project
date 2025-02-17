# Generated by Django 5.1.3 on 2024-12-12 08:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0042_alter_customer_division_alter_product_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='division',
            field=models.CharField(choices=[('Rangpur', 'Rangpur'), ('Dhaka', 'Dhaka'), ('Mymensingh', 'Mymensingh'), ('Barisal', 'Barisal'), ('Khulna', 'Khulna'), ('Sylhet', 'Sylhet'), ('Chittagong', 'Chittagong'), ('Rajshahi', 'Rajshahi')], max_length=100),
        ),
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.CharField(choices=[('CZ', 'Cheese'), ('GH', 'Ghee'), ('LS', 'Lassi'), ('PN', 'Paneer'), ('CR', 'Curd'), ('IC', 'Ice-Creams'), ('ML', 'Milk'), ('MS', 'Milkshake')], max_length=2),
        ),
    ]
