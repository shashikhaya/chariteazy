# Generated by Django 3.2 on 2021-05-04 11:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('causes', '0003_auto_20210504_1141'),
    ]

    operations = [
        migrations.AddField(
            model_name='cause',
            name='vote_count',
            field=models.PositiveIntegerField(null=True),
        ),
    ]
