# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2017-01-22 01:16
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [("challenges", "0012_added_code_name_field")]

    operations = [
        migrations.AlterUniqueTogether(
            name="challengephase",
            unique_together=set([("code_name", "challenge")]),
        )
    ]