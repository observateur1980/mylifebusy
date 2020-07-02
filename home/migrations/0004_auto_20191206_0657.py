# Generated by Django 2.2.7 on 2019-12-06 06:57

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_subcategory_price'),
    ]

    operations = [
        migrations.RenameField(
            model_name='subcategory',
            old_name='view_count',
            new_name='book_count',
        ),
        migrations.AddField(
            model_name='subcategory',
            name='booked_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='subcategory',
            name='created_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='subcategory',
            name='thumbnail_url',
            field=models.CharField(default=django.utils.timezone.now, max_length=400),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='subcategory',
            name='categories',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='subcategory', to='home.Category'),
        ),
    ]
