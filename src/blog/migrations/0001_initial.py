# Generated by Django 2.1.5 on 2019-02-14 14:51

import blog.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='BlogInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('headline', models.CharField(blank=True, max_length=1000, null=True)),
                ('preview_points', models.TextField(blank=True, null=True)),
                ('date_time', models.DateTimeField(auto_now_add=True, null=True)),
                ('last_updated', models.DateTimeField(auto_now=True, null=True)),
                ('age_restricted', models.BooleanField(default=False)),
                ('content', models.TextField(blank=True, null=True)),
                ('image', models.ImageField(blank=True, height_field='height_field', null=True, upload_to=blog.models.get_location, width_field='width_field')),
                ('height_field', models.IntegerField(default=0)),
                ('width_field', models.IntegerField(default=0)),
                ('slug', models.SlugField(blank=True, null=True)),
                ('genre', models.CharField(choices=[('INSPIRATIONAL', 'Inspirational'), ('EDUCATIONAL', 'Educational'), ('ENTERTAINMENT', 'Entertainment'), ('NEWS', 'News'), ('ARINDHAL', 'Arindhal')], default='NEWS', max_length=20)),
                ('likes', models.IntegerField(default=0)),
                ('use_editor', models.BooleanField(default=False)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]