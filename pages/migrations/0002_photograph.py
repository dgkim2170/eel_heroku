# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-05-15 07:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Photograph',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(null=True, upload_to=b'photo/')),
                ('category', models.CharField(choices=[('category1', 'Category1'), ('category4', 'NEWcategory'), ('category2', 'NEWER'), ('code in system', 'name on website')], max_length=255, null=True)),
                ('title', models.CharField(blank=True, max_length=255, null=True)),
                ('description', models.CharField(blank=True, max_length=255, null=True)),
                ('date', models.DateField(blank=True, null=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('made', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
