# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-24 23:19
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('clients', '0004_auto_20170524_0316'),
    ]

    operations = [
        migrations.RenameField(
            model_name='client',
            old_name='client_secret',
            new_name='secret',
        ),
    ]