# Generated by Django 3.1.4 on 2020-12-05 22:51

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forages', '0013_auto_20201205_1750'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entry',
            name='short_comment',
            field=models.TextField(default=datetime.datetime(2020, 12, 5, 17, 51, 16, 764963), help_text='You may type a 255 char short description of your find or leave the current date and time.', max_length=255),
        ),
    ]
