# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0002_productprofile_used'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productprofile',
            name='used',
            field=models.BooleanField(default=True),
        ),
    ]
