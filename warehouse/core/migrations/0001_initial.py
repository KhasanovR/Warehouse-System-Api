# Generated by Django 3.1 on 2022-03-31 09:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Material',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
            options={
                'db_table': 'materials',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('code', models.CharField(max_length=255, unique=True)),
            ],
            options={
                'db_table': 'products',
            },
        ),
        migrations.CreateModel(
            name='Warehouse',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reminder', models.IntegerField(default=0)),
                ('price', models.DecimalField(decimal_places=2, default=None, max_digits=12)),
                ('material', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='warehouses', to='core.material')),
            ],
            options={
                'db_table': 'warehouses',
            },
        ),
        migrations.CreateModel(
            name='ProductMaterial',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(default=1)),
                ('material', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='product_materials', to='core.material')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='product_materials', to='core.product')),
            ],
            options={
                'db_table': 'product_materials',
                'unique_together': {('product', 'material')},
            },
        ),
    ]
