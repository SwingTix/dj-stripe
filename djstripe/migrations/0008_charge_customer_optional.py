# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
class Migration(migrations.Migration):
    dependencies = [
        ('djstripe', '0007_auto_20150625_1243'),
    ]

    operations = [
        migrations.AlterField(
            model_name='charge',
            name='customer',
            field=models.ForeignKey(related_name='charges', to='djstripe.Customer', null=True),
        ),
     ]

