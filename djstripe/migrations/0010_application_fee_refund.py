# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone
import model_utils.fields


class Migration(migrations.Migration):

    dependencies = [
        ('djstripe', '0009_balancetransaction'),
    ]

    operations = [
        migrations.CreateModel(
            name='ApplicationFeeRefund',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, verbose_name='created', editable=False)),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, verbose_name='modified', editable=False)),
                ('stripe_id', models.CharField(unique=True, max_length=50)),
                ('fee', models.CharField(max_length=50, blank=True)),
                ('amount', models.DecimalField(null=True, max_digits=7, decimal_places=2)),
                ('balance_transaction', models.CharField(max_length=50, null=True, blank=True)),
                ('stripe_created', models.DateTimeField()),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
