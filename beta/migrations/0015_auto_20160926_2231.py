# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-09-26 21:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('beta', '0014_auto_20160926_2200'),
    ]

    operations = [
        migrations.AddField(
            model_name='startup',
            name='stat',
            field=models.CharField(choices=[(b'Pending', b'Pending'), (b'Published', b'Published'), (b'Declined', b'Declined')], default='', max_length=30),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='startup',
            name='status',
            field=models.CharField(choices=[(b' ', b' '), (b'Live', b'Live'), (b'Private Beta', b'Private Beta'), (b'Public Beta', b'Public Beta'), (b'Under Development', b'Under Development')], max_length=30),
        ),
    ]
