# Generated by Django 2.1.5 on 2019-02-12 12:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ArindhalContributerInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('added', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated', models.DateTimeField(auto_now=True, null=True)),
                ('slug', models.SlugField(blank=True, null=True)),
                ('name', models.CharField(blank=True, max_length=300, null=True)),
                ('email', models.CharField(blank=True, max_length=500, null=True)),
                ('content', models.CharField(blank=True, max_length=10000, null=True)),
                ('dob', models.DateTimeField(blank=True, null=True)),
            ],
        ),
    ]
