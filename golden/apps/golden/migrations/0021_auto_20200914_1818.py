# Generated by Django 3.1.1 on 2020-09-14 21:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('categorias', '0002_auto_20200914_1648'),
        ('golden', '0020_auto_20200914_1524'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='categoria',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='categorias.categorias'),
        ),
    ]