# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_auto_20151106_1634'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='delete',
            field=models.NullBooleanField(default=False),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='product',
            name='sold',
            field=models.NullBooleanField(default=False),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='product',
            name='time_added',
            field=models.DateTimeField(default=datetime.datetime(2015, 11, 7, 13, 5, 42, 479033)),
            preserve_default=True,
        ),
    ]
