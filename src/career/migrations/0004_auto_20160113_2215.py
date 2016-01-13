# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('career', '0003_auto_20160113_2206'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='image1',
            field=models.ImageField(upload_to=models.CharField(max_length=200)),
        ),
        migrations.AlterField(
            model_name='project',
            name='image2',
            field=models.ImageField(upload_to=models.CharField(max_length=200)),
        ),
    ]
