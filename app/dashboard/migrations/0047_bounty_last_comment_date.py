# Generated by Django 2.0.3 on 2018-03-23 23:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0046_auto_20180319_1329'),
    ]

    operations = [
        migrations.AddField(
            model_name='bounty',
            name='last_comment_date',
            field=models.DateTimeField(null=True),
        ),
    ]
