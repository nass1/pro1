# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-12-09 13:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chinavAPI', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productsmodels',
            name='overview_lst_mod',
            field=models.TextField(),
        ),
    ]
