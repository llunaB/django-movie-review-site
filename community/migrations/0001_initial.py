# Generated by Django 3.2.7 on 2021-09-22 07:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Model',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('movie_title', models.CharField(max_length=20)),
                ('title', models.CharField(max_length=20)),
                ('rank', models.IntegerField()),
                ('content', models.TextField()),
            ],
        ),
    ]
