# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('career', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='image1',
            field=models.ImageField(height_field=262, width_field=218, upload_to=models.SlugField()),
        ),
        migrations.AlterField(
            model_name='project',
            name='image2',
            field=models.ImageField(height_field=262, width_field=218, upload_to=models.SlugField()),
        ),
        migrations.AlterField(
            model_name='project',
            name='image3',
            field=models.ImageField(height_field=262, width_field=218, upload_to=models.SlugField()),
        ),
    ]
