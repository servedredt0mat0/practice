# Generated by Django 3.1.4 on 2020-12-05 23:00

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forages', '0014_auto_20201205_1751'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entry',
            name='foraged_material',
            field=models.CharField(choices=[('Mushroom', 'Mushroom'), ('Shell Foods', 'Shell Foods'), ('Crop', 'Crop'), ('Material', 'Material'), ('In Response', 'In Response')], max_length=255),
        ),
        migrations.AlterField(
            model_name='entry',
            name='short_comment',
            field=models.TextField(default=datetime.datetime(2020, 12, 5, 18, 0, 59, 250278), help_text='You may type a 255 char short description of your find or leave the current date and time.', max_length=255),
        ),
    ]
