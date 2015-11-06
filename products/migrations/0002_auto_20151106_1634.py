# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='time_added',
            field=models.DateTimeField(default=datetime.datetime(2015, 11, 6, 16, 34, 16, 453715)),
            preserve_default=True,
        ),
    ]
