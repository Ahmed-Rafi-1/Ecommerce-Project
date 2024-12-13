# Generated by Django 5.1.4 on 2024-12-10 06:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0008_alter_product_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.CharField(choices=[('LS', 'Lassi'), ('CZ', 'Cheese'), ('PN', 'Paneer'), ('GH', 'Ghee'), ('CR', 'Curd'), ('ML', 'Milk'), ('MS', 'Milkshake'), ('IC', 'Ice-Creams')], max_length=2),
        ),
    ]
