# Generated by Django 3.1.2 on 2020-10-30 00:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('golden', '0035_pedidoproduto_usuario'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pedidoproduto',
            name='usuario',
        ),
    ]
