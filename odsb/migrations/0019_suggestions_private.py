# Generated by Django 2.2.7 on 2020-01-20 11:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('odsb', '0018_post_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='suggestions',
            name='private',
            field=models.BooleanField(default=0),
            preserve_default=False,
        ),
    ]
