# Generated by Django 3.1.1 on 2020-09-10 21:39

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('golden', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Produtos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_produto', models.CharField(max_length=200)),
                ('descricao', models.TextField()),
                ('design_produto', models.TextField()),
                ('categoria', models.CharField(max_length=100)),
                ('data_produto', models.DateTimeField(blank=True, default=datetime.datetime.now)),
            ],
        ),
        migrations.DeleteModel(
            name='Produto',
        ),
    ]