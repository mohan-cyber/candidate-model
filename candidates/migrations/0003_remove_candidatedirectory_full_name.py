# Generated by Django 4.2.7 on 2023-11-20 12:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('candidates', '0002_alter_educationinstitutionmodel_description_and_more'),
    ]

    operations = [
        migrations.RemoveConstraint(
            model_name='candidatedirectory',
            name='full_name',
        ),
    ]
