# Generated by Django 2.1.5 on 2019-03-01 20:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shortenurl', '0002_remove_urlinfo_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='TWMInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('temperature', models.IntegerField(blank=True, null=True)),
            ],
        ),
    ]
