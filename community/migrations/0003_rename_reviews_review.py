# Generated by Django 3.2.6 on 2021-09-22 09:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('community', '0002_rename_model_reviews'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Reviews',
            new_name='Review',
        ),
    ]
