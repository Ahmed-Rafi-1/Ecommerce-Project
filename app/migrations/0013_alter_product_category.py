# Generated by Django 5.1.4 on 2024-12-10 10:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0012_alter_product_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.CharField(choices=[('IC', 'Ice-Creams'), ('LS', 'Lassi'), ('MS', 'Milkshake'), ('CR', 'Curd'), ('PN', 'Paneer'), ('GH', 'Ghee'), ('ML', 'Milk'), ('CZ', 'Cheese')], max_length=2),
        ),
    ]
