# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-09-02 08:11
from __future__ import unicode_literals

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('core', '0002_load_data'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='resultfile',
            name='result',
        ),
        migrations.AddField(
            model_name='resultfile',
            name='run',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='files',
                                    to='core.TestRun'),
            preserve_default=False,
        ),
    ]
