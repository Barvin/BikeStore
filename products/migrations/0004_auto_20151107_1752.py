# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_auto_20151107_1305'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='time_added',
            field=models.DateTimeField(default=datetime.datetime(2015, 11, 7, 17, 52, 24, 511502)),
            preserve_default=True,
        ),
    ]
