# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('challenge', '0003_significantother_gender'),
    ]

    operations = [
        migrations.AlterField(
            model_name='goalinstance',
            name='started',
            field=models.DateField(),
            preserve_default=True,
        ),
    ]
