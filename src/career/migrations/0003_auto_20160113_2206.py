# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('career', '0002_auto_20160113_2159'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='image1',
            field=models.ImageField(upload_to=models.SlugField()),
        ),
        migrations.AlterField(
            model_name='project',
            name='image2',
            field=models.ImageField(upload_to=models.SlugField()),
        ),
        migrations.AlterField(
            model_name='project',
            name='image3',
            field=models.ImageField(upload_to=models.SlugField()),
        ),
    ]
