# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-10-24 18:57
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('college', '0002_auto_20171024_1455'),
    ]

    operations = [
        migrations.RenameField(
            model_name='student',
            old_name='course',
            new_name='cour',
        ),
        migrations.RenameField(
            model_name='student_attendance',
            old_name='student',
            new_name='stud',
        ),
        migrations.RenameField(
            model_name='subject',
            old_name='course',
            new_name='cour',
        ),
    ]
