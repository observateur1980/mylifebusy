# Generated by Django 2.2.7 on 2019-12-06 08:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0007_remove_subcategory_thumbnail_url'),
    ]

    operations = [
        migrations.RenameField(
            model_name='subcategory',
            old_name='img',
            new_name='cover_img',
        ),
    ]
