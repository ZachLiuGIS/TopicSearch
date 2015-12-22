# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone
import model_utils.fields


class Migration(migrations.Migration):

    dependencies = [
        ('topic_search', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='searchtopic',
            name='created',
            field=model_utils.fields.AutoCreatedField(editable=False, verbose_name='created', default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='searchtopic',
            name='modified',
            field=model_utils.fields.AutoLastModifiedField(editable=False, verbose_name='modified', default=django.utils.timezone.now),
        ),
    ]
