# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=500)),
                ('time_added', models.DateTimeField(default=datetime.datetime(2015, 11, 6, 0, 32, 9, 155719))),
                ('image', models.CharField(max_length=500, null=True, blank=True)),
                ('description', models.TextField(max_length=5000, null=True, blank=True)),
                ('price', models.FloatField(default=0, max_length=10)),
                ('sold', models.NullBooleanField()),
                ('delete', models.NullBooleanField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
