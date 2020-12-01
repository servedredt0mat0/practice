# Generated by Django 3.1.4 on 2020-12-01 22:05

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('forages', '0002_entry_count_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='entry',
            name='short_comment',
            field=models.CharField(default=django.utils.timezone.now, help_text='You may type a 112 char short description of your find.', max_length=112),
            preserve_default=False,
        ),
    ]
