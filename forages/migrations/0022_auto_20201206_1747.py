# Generated by Django 3.1.4 on 2020-12-06 22:47

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forages', '0021_auto_20201206_1732'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entry',
            name='short_comment',
            field=models.TextField(default=datetime.datetime(2020, 12, 6, 17, 47, 26, 396746), help_text='You may type a 512 char short description of your find or leave the current date and time.', max_length=512),
        ),
    ]
