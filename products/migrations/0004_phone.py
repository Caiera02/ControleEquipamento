# Generated by Django 5.0 on 2024-11-06 14:38

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_product_memory_ram_product_processor_product_storage'),
    ]

    operations = [
        migrations.CreateModel(
            name='Phone',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Nome')),
                ('storage', models.CharField(max_length=10, verbose_name='Armazenamento')),
                ('is_active', models.BooleanField(default=True, verbose_name='Ativo')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Descrição')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Criado em')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Atualizado em')),
                ('brand', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='phon', to='products.brand', verbose_name='Marca')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='phone', to='products.category', verbose_name='Departamento')),
            ],
            options={
                'verbose_name': 'Teste',
                'ordering': ['title'],
            },
        ),
    ]