# Generated by Django 5.1.4 on 2024-12-10 07:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0009_alter_product_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.CharField(choices=[('GH', 'Ghee'), ('IC', 'Ice-Creams'), ('CR', 'Curd'), ('ML', 'Milk'), ('CZ', 'Cheese'), ('MS', 'Milkshake'), ('PN', 'Paneer'), ('LS', 'Lassi')], max_length=2),
        ),
    ]
