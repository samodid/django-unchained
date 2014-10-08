# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('stories', '0002_auto_20141007_1310'),
    ]

    operations = [
        migrations.AddField(
            model_name='story',
            name='voters',
            field=models.ManyToManyField(related_name=b'liked_stories', to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='story',
            name='moderator',
            field=models.ForeignKey(related_name=b'moderated_stories', to=settings.AUTH_USER_MODEL),
        ),
    ]
