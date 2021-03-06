# Generated by Django 2.2.7 on 2019-12-09 09:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0010_auto_20191206_1411'),
    ]

    operations = [
        migrations.CreateModel(
            name='CareerMail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.CharField(max_length=20)),
                ('looking_for', models.CharField(max_length=200)),
                ('document', models.FileField(upload_to='documents/')),
                ('reference', models.CharField(max_length=300)),
            ],
        ),
    ]
