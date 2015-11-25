# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_someuser_is_staff'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='someuser',
            name='is_staff',
        ),
        migrations.AlterField(
            model_name='someuser',
            name='joined',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
    ]
