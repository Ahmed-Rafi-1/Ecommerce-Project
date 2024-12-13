# Generated by Django 5.1.3 on 2024-12-12 09:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0047_alter_customer_division_alter_product_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='division',
            field=models.CharField(choices=[('Rajshahi', 'Rajshahi'), ('Khulna', 'Khulna'), ('Sylhet', 'Sylhet'), ('Chittagong', 'Chittagong'), ('Mymensingh', 'Mymensingh'), ('Barisal', 'Barisal'), ('Dhaka', 'Dhaka'), ('Rangpur', 'Rangpur')], max_length=100),
        ),
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.CharField(choices=[('PN', 'Paneer'), ('ML', 'Milk'), ('CR', 'Curd'), ('IC', 'Ice-Creams'), ('GH', 'Ghee'), ('CZ', 'Cheese'), ('MS', 'Milkshake'), ('LS', 'Lassi')], max_length=2),
        ),
    ]
