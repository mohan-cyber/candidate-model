# Generated by Django 4.2.7 on 2023-11-20 13:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('candidates', '0005_alter_candidatedirectory_contact_no_alternate_and_more'),
    ]

    operations = [
        migrations.RemoveConstraint(
            model_name='candidatedirectory',
            name='full_name',
        ),
    ]
