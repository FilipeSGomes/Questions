# Generated by Django 3.1.1 on 2020-09-13 13:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categorias',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_categoria', models.CharField(choices=[('Blusa de Moletom', 'Blusa de Moletom'), ('Calça de Sarja', 'Calça de Sarja'), ('Camisetas', 'Camisetas'), ('Bonés', 'Bonés'), ('Blusa corta-vento', 'Blusa corta-vento'), ('Calça de Moletom', 'Calça de Moletom'), ('Acessórios', 'Acessórios'), ('Jaquetas', 'Jaquetas'), ('Calçados', 'Calçados')], max_length=50, unique=True, verbose_name='Categoria')),
            ],
        ),
    ]