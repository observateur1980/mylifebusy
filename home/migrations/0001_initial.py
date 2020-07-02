# Generated by Django 2.2.7 on 2019-12-04 00:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=40)),
                ('thumbnail_url', models.CharField(max_length=400)),
                ('active', models.BooleanField(default=False)),
                ('icon', models.CharField(default='<i class="im im-wrench"></i>', max_length=100)),
            ],
            options={
                'verbose_name': 'category',
                'verbose_name_plural': 'categories',
            },
        ),
        migrations.CreateModel(
            name='Icon',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=40)),
                ('icon_tag', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name': 'icon',
                'verbose_name_plural': 'icons',
            },
        ),
        migrations.CreateModel(
            name='SubCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('view_count', models.IntegerField(default=0)),
                ('categories', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.Category')),
                ('icon', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.Icon')),
            ],
            options={
                'verbose_name': 'subcategory',
                'verbose_name_plural': 'subcategories',
            },
        ),
    ]