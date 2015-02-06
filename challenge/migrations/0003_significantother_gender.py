# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('challenge', '0002_significantother'),
    ]

    operations = [
        migrations.AddField(
            model_name='significantother',
            name='gender',
            field=models.CharField(default='MA', max_length=2, choices=[(b'MA', b'male'), (b'FE', b'female')]),
            preserve_default=False,
        ),
    ]
