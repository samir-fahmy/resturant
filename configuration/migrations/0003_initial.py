# Generated by Django 5.0.3 on 2024-05-16 14:14

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('configuration', '0002_delete_userr'),
    ]

    operations = [
        migrations.CreateModel(
            name='Items_type',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_lo', models.CharField(max_length=50, verbose_name='الإسم المحلى')),
                ('name_fk', models.CharField(max_length=50, verbose_name='الإسم الأجنبى')),
            ],
        ),
        migrations.CreateModel(
            name='Store',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_lo', models.CharField(max_length=50, verbose_name='الإسم المحلى')),
                ('name_fk', models.CharField(max_length=50, verbose_name='الإسم الأجنبى')),
                ('is_stop', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Unit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_lo', models.CharField(max_length=50, verbose_name='الإسم المحلى')),
                ('name_fk', models.CharField(max_length=50, verbose_name='الإسم الأجنبى')),
                ('codeUnit', models.CharField(max_length=50, verbose_name='رمز الوحده')),
            ],
        ),
        migrations.CreateModel(
            name='Items',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('barcode', models.CharField(max_length=50, verbose_name='باركود')),
                ('items_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='configuration.items_type')),
                ('unit', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='configuration.unit')),
            ],
        ),
        migrations.CreateModel(
            name='story_items',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('qty', models.IntegerField(verbose_name='الكمية')),
                ('date_in', models.DateTimeField(verbose_name='تاريخ الإضافه')),
                ('items', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='configuration.items')),
                ('stor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='configuration.store')),
            ],
        ),
    ]
