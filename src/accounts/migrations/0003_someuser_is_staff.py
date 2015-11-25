# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_someuser_is_superuser'),
    ]

    operations = [
        migrations.AddField(
            model_name='someuser',
            name='is_staff',
            field=models.BooleanField(default=False),
        ),
    ]
