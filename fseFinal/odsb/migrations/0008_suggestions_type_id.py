# Generated by Django 2.2.7 on 2019-12-23 11:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('odsb', '0007_suggestions'),
    ]

    operations = [
        migrations.AddField(
            model_name='suggestions',
            name='type_id',
            field=models.CharField(default=0, max_length=100),
            preserve_default=False,
        ),
    ]
