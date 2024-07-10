# Generated by Django 5.0.6 on 2024-07-10 21:30

import sorl.thumbnail.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Items',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='نام کالا')),
                ('category', models.CharField(choices=[('sport', 'sport'), ('classic', 'classic'), ('normal', 'normal'), ('modern', 'modern'), ('new', 'new'), ('old', 'old'), ('racing', 'racing'), ('other', 'other')], max_length=10, verbose_name='دسته بندی')),
                ('image', sorl.thumbnail.fields.ImageField(upload_to='media/images/', verbose_name='تصویر')),
                ('brand', models.CharField(max_length=25, verbose_name='شرکت سازنده')),
                ('available', models.BooleanField(default=True, verbose_name='موجود')),
                ('number', models.IntegerField(verbose_name='موجودی')),
                ('price', models.IntegerField(verbose_name='قیمت')),
                ('description', models.TextField(max_length=1000, verbose_name='توضیحات')),
                ('info', models.TextField(blank=True, max_length=10000, null=True, verbose_name='مشخصات')),
                ('views', models.IntegerField(default=0)),
                ('boughts', models.IntegerField(default=0)),
                ('slug', models.SlugField(unique=True, verbose_name='لینک مایه')),
            ],
            options={
                'verbose_name': 'کالاها',
            },
        ),
    ]
