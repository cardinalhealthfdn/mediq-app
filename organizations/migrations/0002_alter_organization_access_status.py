# Generated by Django 5.0.1 on 2024-01-29 21:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('organizations', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='organization',
            name='access_status',
            field=models.CharField(choices=[('access_granted', 'access_granted'), ('access_suspended', 'access_suspended'), ('access_banned', 'access_banned')], max_length=25),
        ),
    ]
