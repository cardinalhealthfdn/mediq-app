# Generated by Django 5.0.1 on 2024-01-30 10:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('organizations', '0002_alter_organization_access_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='organization',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
    ]
