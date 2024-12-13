# Generated by Django 5.1.4 on 2024-12-10 07:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0010_alter_product_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.CharField(choices=[('IC', 'Ice-Creams'), ('MS', 'Milkshake'), ('ML', 'Milk'), ('LS', 'Lassi'), ('CR', 'Curd'), ('CZ', 'Cheese'), ('PN', 'Paneer'), ('GH', 'Ghee')], max_length=2),
        ),
    ]
