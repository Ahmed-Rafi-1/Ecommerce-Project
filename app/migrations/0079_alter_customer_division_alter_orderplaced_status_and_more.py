# Generated by Django 5.1.4 on 2024-12-13 03:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0078_alter_customer_division_alter_orderplaced_status_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='division',
            field=models.CharField(choices=[('Chittagong', 'Chittagong'), ('Rangpur', 'Rangpur'), ('Sylhet', 'Sylhet'), ('Mymensingh', 'Mymensingh'), ('Dhaka', 'Dhaka'), ('Barisal', 'Barisal'), ('Rajshahi', 'Rajshahi'), ('Khulna', 'Khulna')], max_length=100),
        ),
        migrations.AlterField(
            model_name='orderplaced',
            name='status',
            field=models.CharField(choices=[('Cancle', 'Cancle'), ('Pending', 'Pending'), ('Accepted', 'Accepted'), ('Packed', 'Packed'), ('Delivered', 'Delivered'), ('On The Way', 'On The Way')], default='Pending', max_length=50),
        ),
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.CharField(choices=[('IC', 'Ice-Creams'), ('PN', 'Paneer'), ('LS', 'Lassi'), ('MS', 'Milkshake'), ('CR', 'Curd'), ('GH', 'Ghee'), ('ML', 'Milk'), ('CZ', 'Cheese')], max_length=2),
        ),
    ]
