# Generated by Django 3.2.8 on 2022-10-03 10:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0013_remove_product_category'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='cat',
        ),
        migrations.AddField(
            model_name='product',
            name='category',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.DeleteModel(
            name='Category',
        ),
    ]