# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=200)),
                ('name', models.CharField(max_length=100, blank=True)),
                ('details', models.TextField()),
                ('implementation', models.CharField(max_length=200, blank=True)),
                ('features', models.TextField()),
                ('tools', models.TextField()),
                ('slug', models.SlugField()),
                ('image1', models.ImageField(upload_to=models.SlugField())),
                ('image2', models.ImageField(upload_to=models.SlugField())),
                ('image3', models.ImageField(upload_to=models.SlugField())),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
