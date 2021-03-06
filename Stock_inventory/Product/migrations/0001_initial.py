# Generated by Django 3.2.3 on 2021-05-23 12:53

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Product Name')),
                ('spec', models.TextField(blank=True, verbose_name='Product Specification')),
                ('slug', models.SlugField(blank=True, verbose_name='Product Slug')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Created at')),
            ],
        ),
        migrations.CreateModel(
            name='ProductImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image_name', models.CharField(max_length=50, verbose_name='Image Name')),
                ('description', models.TextField(max_length=255, verbose_name='Product Description')),
                ('image', models.ImageField(upload_to='protected/None/', verbose_name='Product Image')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Created at')),
            ],
        ),
        migrations.CreateModel(
            name='Stock',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(verbose_name='Stock Quantity')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Created at')),
            ],
        ),
        migrations.CreateModel(
            name='Supplier',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_name', models.CharField(max_length=50, unique=True, verbose_name='Company Name')),
                ('address', models.TextField(verbose_name='Company Address')),
                ('contact_no', models.CharField(max_length=11, validators=[django.core.validators.RegexValidator('^[0-9]{10,11}$', 'Please enter a valid phone number')], verbose_name='Contact Number')),
                ('contact_person', models.CharField(max_length=254, verbose_name='Contact Person')),
                ('slug', models.SlugField(blank=True, verbose_name='Supplier Slug')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Created at')),
            ],
        ),
    ]
