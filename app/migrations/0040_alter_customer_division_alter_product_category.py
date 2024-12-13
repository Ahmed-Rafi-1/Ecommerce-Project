# Generated by Django 5.1.3 on 2024-12-12 08:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0039_alter_customer_division_alter_product_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='division',
            field=models.CharField(choices=[('Rajshahi', 'Rajshahi'), ('Khulna', 'Khulna'), ('Barisal', 'Barisal'), ('Mymensingh', 'Mymensingh'), ('Dhaka', 'Dhaka'), ('Chittagong', 'Chittagong'), ('Rangpur', 'Rangpur'), ('Sylhet', 'Sylhet')], max_length=100),
        ),
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.CharField(choices=[('CZ', 'Cheese'), ('PN', 'Paneer'), ('CR', 'Curd'), ('LS', 'Lassi'), ('IC', 'Ice-Creams'), ('MS', 'Milkshake'), ('ML', 'Milk'), ('GH', 'Ghee')], max_length=2),
        ),
    ]
