# Generated by Django 2.2.7 on 2019-12-23 12:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('odsb', '0008_suggestions_type_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='suggestions',
            name='given_date',
        ),
    ]
