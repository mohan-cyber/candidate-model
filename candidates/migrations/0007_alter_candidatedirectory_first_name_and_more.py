# Generated by Django 4.2.7 on 2023-11-20 13:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('candidates', '0006_remove_candidatedirectory_full_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='candidatedirectory',
            name='first_name',
            field=models.CharField(blank=True, max_length=255, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='candidatedirectory',
            name='last_name',
            field=models.CharField(blank=True, max_length=255, null=True, unique=True),
        ),
    ]
