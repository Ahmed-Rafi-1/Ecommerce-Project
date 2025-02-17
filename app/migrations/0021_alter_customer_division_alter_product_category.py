# Generated by Django 5.1.4 on 2024-12-10 12:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0020_alter_customer_division_alter_product_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='division',
            field=models.CharField(choices=[('Chittagong', 'Chittagong'), ('Barisal', 'Barisal'), ('Mymensingh', 'Mymensingh'), ('Rajshahi', 'Rajshahi'), ('Dhaka', 'Dhaka'), ('Rangpur', 'Rangpur'), ('Khulna', 'Khulna'), ('Sylhet', 'Sylhet')], max_length=100),
        ),
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.CharField(choices=[('ML', 'Milk'), ('CR', 'Curd'), ('MS', 'Milkshake'), ('LS', 'Lassi'), ('PN', 'Paneer'), ('IC', 'Ice-Creams'), ('CZ', 'Cheese'), ('GH', 'Ghee')], max_length=2),
        ),
    ]
