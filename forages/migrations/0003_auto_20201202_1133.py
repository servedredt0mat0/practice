# Generated by Django 3.1.4 on 2020-12-02 16:33

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forages', '0002_auto_20201202_1131'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entry',
            name='short_comment',
            field=models.TextField(default=datetime.datetime(2020, 12, 2, 11, 33, 11, 422847), help_text='You may type a 112 char short description of your find or leave the current date and time.', max_length=112),
        ),
    ]
