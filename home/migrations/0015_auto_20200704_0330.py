# Generated by Django 3.0.8 on 2020-07-04 03:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0014_auto_20200704_0244'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contact',
            name='age',
        ),
        migrations.RemoveField(
            model_name='contact',
            name='start_date',
        ),
    ]
