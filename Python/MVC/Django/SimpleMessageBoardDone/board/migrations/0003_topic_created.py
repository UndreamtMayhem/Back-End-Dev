# Generated by Django 2.0.2 on 2018-04-23 16:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0002_remove_topic_created'),
    ]

    operations = [
        migrations.AddField(
            model_name='topic',
            name='created',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
