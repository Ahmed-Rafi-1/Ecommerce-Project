# Generated by Django 5.1.3 on 2024-12-12 18:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0065_alter_customer_division_alter_orderplaced_status_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='division',
            field=models.CharField(choices=[('Dhaka', 'Dhaka'), ('Chittagong', 'Chittagong'), ('Barisal', 'Barisal'), ('Rangpur', 'Rangpur'), ('Mymensingh', 'Mymensingh'), ('Rajshahi', 'Rajshahi'), ('Sylhet', 'Sylhet'), ('Khulna', 'Khulna')], max_length=100),
        ),
        migrations.AlterField(
            model_name='orderplaced',
            name='status',
            field=models.CharField(choices=[('Accepted', 'Accepted'), ('Delivered', 'Delivered'), ('Packed', 'Packed'), ('On The Way', 'On The Way'), ('Pending', 'Pending'), ('Cancle', 'Cancle')], default='Pending', max_length=50),
        ),
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.CharField(choices=[('ML', 'Milk'), ('GH', 'Ghee'), ('MS', 'Milkshake'), ('IC', 'Ice-Creams'), ('PN', 'Paneer'), ('LS', 'Lassi'), ('CR', 'Curd'), ('CZ', 'Cheese')], max_length=2),
        ),
    ]
