# Generated by Django 3.2.8 on 2022-10-14 08:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0015_product_prod_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.IntegerField(),
        ),
    ]