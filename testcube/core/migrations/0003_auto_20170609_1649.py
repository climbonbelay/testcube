# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-06-09 08:49
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ('core', '0002_auto_20170607_1142'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Project',
            new_name='Team',
        ),
        migrations.AlterModelOptions(
            name='configuration',
            options={'ordering': ['id']},
        ),
        migrations.AlterModelOptions(
            name='issue',
            options={'ordering': ['-created_on']},
        ),
        migrations.AlterModelOptions(
            name='product',
            options={'ordering': ['id']},
        ),
        migrations.AlterModelOptions(
            name='resultanalysis',
            options={'ordering': ['-updated_on']},
        ),
        migrations.AlterModelOptions(
            name='team',
            options={'ordering': ['id']},
        ),
        migrations.AlterModelOptions(
            name='testcase',
            options={'ordering': ['id']},
        ),
        migrations.AlterModelOptions(
            name='testclient',
            options={'ordering': ['id']},
        ),
        migrations.AlterModelOptions(
            name='testresult',
            options={'ordering': ['start_time']},
        ),
        migrations.AlterModelOptions(
            name='testrun',
            options={'ordering': ['-id']},
        ),
        migrations.RenameField(
            model_name='testrun',
            old_name='project',
            new_name='team',
        ),
    ]
