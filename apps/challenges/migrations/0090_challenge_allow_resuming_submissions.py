# Generated by Django 2.2.20 on 2023-06-13 20:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('challenges', '0089_add_challenge_use_host_sqs'),
    ]

    operations = [
        migrations.AddField(
            model_name='challenge',
            name='allow_resuming_submissions',
            field=models.BooleanField(default=False),
        ),
    ]
