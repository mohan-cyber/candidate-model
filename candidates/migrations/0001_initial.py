# Generated by Django 4.2.7 on 2023-11-20 06:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CityModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('country', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='EducationInstitutionModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('education_institution', models.CharField(max_length=255)),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='EducationLevelModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('level', models.CharField(max_length=50)),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='EducationQualificationModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('qualification', models.CharField(max_length=255)),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='EducationSpecializationModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('specialization', models.CharField(max_length=255)),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='EmployeeDirectoryModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('employee_id', models.CharField(max_length=20, unique=True)),
                ('first_name', models.CharField(max_length=255)),
                ('last_name', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='EventDetailsModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('date', models.DateField()),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='ExperienceLevelModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('level', models.CharField(max_length=50)),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='GenderModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='JobRequisitionModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('department', models.CharField(max_length=255)),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='MaritalStatusModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='PersonaModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='ReasonForChangeModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reason', models.CharField(max_length=255)),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='ScreeningModeModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='SourceModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='SourceTypeModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Candidatedirectory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('recruiter_alert', models.CharField(blank=True, max_length=50, null=True)),
                ('first_name', models.CharField(blank=True, max_length=255, null=True)),
                ('last_name', models.CharField(blank=True, max_length=255, null=True)),
                ('email', models.CharField(blank=True, max_length=50, null=True)),
                ('role', models.IntegerField(blank=True, null=True)),
                ('dob', models.DateField(blank=True, null=True)),
                ('contact_no_primary', models.DecimalField(blank=True, decimal_places=0, max_digits=10, null=True)),
                ('contact_no_alternate', models.DecimalField(blank=True, decimal_places=0, max_digits=10, null=True)),
                ('referred_by_other', models.CharField(blank=True, max_length=250, null=True)),
                ('address_line', models.CharField(blank=True, max_length=255, null=True)),
                ('pincode', models.DecimalField(blank=True, decimal_places=0, max_digits=6, null=True)),
                ('education_specialization_other', models.TextField(blank=True, null=True)),
                ('education_institution_other', models.TextField(blank=True, null=True)),
                ('years_of_experience', models.DecimalField(blank=True, decimal_places=2, max_digits=4, null=True)),
                ('current_employer', models.CharField(blank=True, max_length=100, null=True)),
                ('current_designation', models.TextField(blank=True, null=True)),
                ('current_monthly_salary', models.IntegerField(blank=True, null=True)),
                ('expected_monthly_salary', models.IntegerField(blank=True, null=True)),
                ('notice_period', models.CharField(blank=True, max_length=50, null=True)),
                ('photo_path', models.TextField(blank=True, null=True)),
                ('resume_path', models.TextField(blank=True, null=True)),
                ('login_time', models.DateTimeField(blank=True, null=True)),
                ('logout_time', models.DateTimeField(blank=True, null=True)),
                ('ip_address', models.CharField(blank=True, max_length=15, null=True)),
                ('geo_location', models.CharField(blank=True, max_length=50, null=True)),
                ('created_date', models.DateTimeField(blank=True, null=True)),
                ('created_by', models.IntegerField(blank=True, null=True)),
                ('modified_date', models.DateTimeField(blank=True, null=True)),
                ('modified_by', models.IntegerField(blank=True, null=True)),
                ('status', models.IntegerField(default=1)),
                ('city', models.ForeignKey(blank=True, db_column='city', null=True, on_delete=django.db.models.deletion.SET_NULL, to='candidates.citymodel')),
                ('education_institution', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='candidates.educationinstitutionmodel')),
                ('education_qualification', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='candidates.educationqualificationmodel')),
                ('education_specialization', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='candidates.educationspecializationmodel')),
                ('event', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='candidates.eventdetailsmodel')),
                ('experience_level', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='candidates.experiencelevelmodel')),
                ('gender', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='candidates.gendermodel')),
                ('job_position', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='candidates.jobrequisitionmodel')),
                ('marital_status', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='candidates.maritalstatusmodel')),
                ('persona', models.ForeignKey(blank=True, default=1, null=True, on_delete=django.db.models.deletion.SET_NULL, to='candidates.personamodel')),
                ('reason_for_change', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='candidates.reasonforchangemodel')),
                ('referred_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='candidates.employeedirectorymodel')),
                ('screening_mode', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='candidates.screeningmodemodel')),
                ('source', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='source_for_candidate_details', to='candidates.sourcemodel')),
                ('source_type', models.ForeignKey(blank=True, db_column='source_type', null=True, on_delete=django.db.models.deletion.SET_NULL, to='candidates.sourcetypemodel')),
            ],
            options={
                'db_table': 'candidate_directory',
            },
        ),
        migrations.AddConstraint(
            model_name='candidatedirectory',
            constraint=models.UniqueConstraint(fields=('first_name', 'last_name'), name='full_name'),
        ),
    ]
