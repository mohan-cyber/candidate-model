# Generated by Django 4.2.7 on 2023-11-20 12:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('candidates', '0004_remove_employeedirectorymodel_employee_id_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='candidatedirectory',
            name='contact_no_alternate',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='candidatedirectory',
            name='contact_no_primary',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='candidatedirectory',
            name='pincode',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='candidatedirectory',
            name='years_of_experience',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
    ]
