# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-05-10 01:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Navigate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=8, verbose_name=b'\xe5\xaf\xbc\xe8\x88\xaa\xe5\x90\x8d\xe7\xa7\xb0')),
                ('description', models.CharField(max_length=50, verbose_name=b'\xe5\xaf\xbc\xe8\x88\xaa\xe6\x8f\x8f\xe8\xbf\xb0')),
                ('navurl', models.CharField(max_length=64, verbose_name=b'url')),
                ('index', models.IntegerField(default=999, verbose_name=b'\xe6\x8e\x92\xe5\x88\x97\xe9\xa1\xba\xe5\xba\x8f(\xe4\xbb\x8e\xe5\xb0\x8f\xe5\x88\xb0\xe5\xa4\xa7)')),
            ],
            options={
                'ordering': ['index', 'id'],
                'verbose_name': '\u5bfc\u822a',
                'verbose_name_plural': '\u5bfc\u822a',
            },
        ),
    ]