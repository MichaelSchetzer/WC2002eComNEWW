# Generated by Django 3.2.8 on 2022-09-29 16:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0011_auto_20220929_1928'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='cat_id',
            new_name='cat',
        ),
    ]
