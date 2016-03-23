# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone
import model_utils.fields


class Migration(migrations.Migration):

    dependencies = [
        ('djstripe', '0008_charge_customer_optional'),
    ]

    operations = [
        migrations.CreateModel(
            name='BalanceTransaction',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, verbose_name='created', editable=False)),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, verbose_name='modified', editable=False)),
                ('stripe_id', models.CharField(unique=True, max_length=50)),
                ('amount', models.DecimalField(null=True, max_digits=7, decimal_places=2)),
                ('fee', models.DecimalField(null=True, max_digits=7, decimal_places=2)),
                ('net', models.DecimalField(null=True, max_digits=7, decimal_places=2)),
                ('stripe_created', models.DateTimeField()),
                ('source', models.CharField(max_length=50, blank=True)),
                ('description', models.TextField(blank=True)),
                ('application_fee', models.DecimalField(null=True, max_digits=7, decimal_places=2)),
                ('stripe_fee', models.DecimalField(null=True, max_digits=7, decimal_places=2)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='charge',
            name='balance_transaction',
            field=models.CharField(max_length=50, blank=True, null=True),
        ),
        migrations.CreateModel(
            name='Refund',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, verbose_name='created', editable=False)),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, verbose_name='modified', editable=False)),
                ('stripe_id', models.CharField(unique=True, max_length=50)),
                ('amount', models.DecimalField(null=True, max_digits=7, decimal_places=2)),
                ('balance_transaction', models.CharField(max_length=50, null=True, blank=True)),
                ('charge', models.CharField(max_length=50, blank=True)),
                ('stripe_created', models.DateTimeField()),
                ('reason', models.CharField(max_length=20, blank=True, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ApplicationFee',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, verbose_name='created', editable=False)),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, verbose_name='modified', editable=False)),
                ('stripe_id', models.CharField(unique=True, max_length=50)),
                ('account', models.CharField(max_length=50, blank=True)),
                ('amount', models.DecimalField(null=True, max_digits=7, decimal_places=2)),
                ('amount_refunded', models.DecimalField(null=True, max_digits=7, decimal_places=2)),
                ('balance_transaction', models.CharField(max_length=50, null=True, blank=True)),
                ('charge', models.CharField(max_length=50, blank=True)),
                ('stripe_created', models.DateTimeField()),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
