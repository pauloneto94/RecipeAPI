# Generated by Django 3.0.7 on 2020-06-23 20:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_ingridient'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Ingridient',
            new_name='Ingredient',
        ),
    ]
