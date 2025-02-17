# Generated by Django 5.1.4 on 2024-12-10 12:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0022_alter_customer_division_alter_product_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='division',
            field=models.CharField(choices=[('Chittagong', 'Chittagong'), ('Barisal', 'Barisal'), ('Rajshahi', 'Rajshahi'), ('Dhaka', 'Dhaka'), ('Sylhet', 'Sylhet'), ('Mymensingh', 'Mymensingh'), ('Khulna', 'Khulna'), ('Rangpur', 'Rangpur')], max_length=100),
        ),
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.CharField(choices=[('MS', 'Milkshake'), ('IC', 'Ice-Creams'), ('PN', 'Paneer'), ('ML', 'Milk'), ('GH', 'Ghee'), ('LS', 'Lassi'), ('CR', 'Curd'), ('CZ', 'Cheese')], max_length=2),
        ),
    ]
