# Generated by Django 3.1.2 on 2020-10-09 02:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('categorias', '0005_auto_20201008_2318'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='categoria',
            name='sub_categoria',
        ),
    ]