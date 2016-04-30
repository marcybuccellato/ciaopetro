# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-03-28 18:14
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('flatpages', '0001_initial'),
        ('blog', '0010_post_tags'),
    ]

    operations = [
        migrations.CreateModel(
            name='CiaoPetroFlatPage',
            fields=[
                ('flatpage_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='flatpages.FlatPage')),
                ('featured_image', models.ImageField(blank=True, null=True, upload_to=b'photos/%Y/%m/%d')),
            ],
            bases=('flatpages.flatpage',),
        ),
    ]