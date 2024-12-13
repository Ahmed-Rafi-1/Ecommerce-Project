# Generated by Django 5.1.4 on 2024-12-09 18:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_alter_product_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.CharField(choices=[('LS', 'Lassi'), ('CR', 'Curd'), ('cz', 'Cheese'), ('IC', 'Ice-Creams'), ('MS', 'Milkshake'), ('PN', 'Paneer'), ('GH', 'Ghee'), ('ML', 'Milk')], max_length=2),
        ),
    ]
