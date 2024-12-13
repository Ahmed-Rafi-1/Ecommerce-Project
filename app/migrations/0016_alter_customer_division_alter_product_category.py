# Generated by Django 5.1.4 on 2024-12-10 11:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0015_alter_customer_division_alter_product_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='division',
            field=models.CharField(choices=[('Khulna', 'Khulna'), ('Rajshahi', 'Rajshahi'), ('Dhaka', 'Dhaka'), ('Barisal', 'Barisal'), ('Sylhet', 'Sylhet'), ('Rangpur', 'Rangpur'), ('Mymensingh', 'Mymensingh'), ('Chittagong', 'Chittagong')], max_length=100),
        ),
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.CharField(choices=[('CZ', 'Cheese'), ('PN', 'Paneer'), ('IC', 'Ice-Creams'), ('ML', 'Milk'), ('GH', 'Ghee'), ('MS', 'Milkshake'), ('CR', 'Curd'), ('LS', 'Lassi')], max_length=2),
        ),
    ]
