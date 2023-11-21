from django.db import models


class EventDetailsModel(models.Model):
    name = models.CharField(max_length=255)
    date = models.DateField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return str(self.name)


class JobRequisitionModel(models.Model):
    title = models.CharField(max_length=255)
    department = models.CharField(max_length=255, blank=True, null=True)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return str(self.title)


class PersonaModel(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return str(self.name)


class ScreeningModeModel(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return str(self.name)


class GenderModel(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return str(self.name)


class MaritalStatusModel(models.Model):
    status = models.CharField(max_length=50)

    def __str__(self):
        return str(self.status)


class EmployeeDirectoryModel(models.Model):
    # employee_id = models.CharField(max_length=20, unique=True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField()

    def __str__(self):
        return str(self.email)


class CityModel(models.Model):
    name = models.CharField(max_length=255)
    country = models.CharField(max_length=255)

    def __str__(self):
        return str(self.name)


class ExperienceLevelModel(models.Model):
    level = models.CharField(max_length=50)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return str(self.level)


class EducationLevelModel(models.Model):
    level = models.CharField(max_length=50)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return str(self.level)


class EducationQualificationModel(models.Model):
    qualification = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return str(self.qualification)


class EducationSpecializationModel(models.Model):
    specialization = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return str(self.specialization)


class EducationInstitutionModel(models.Model):
    education_institution = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return str(self.education_institution)


class SourceModel(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return str(self.name)


class SourceTypeModel(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return str(self.name)


class ReasonForChangeModel(models.Model):
    reason = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return str(self.reason)


class Candidatedirectory(models.Model):
    event = models.ForeignKey(
        EventDetailsModel, on_delete=models.SET_NULL, blank=True, null=True
    )
    job_position = models.ForeignKey(
        JobRequisitionModel,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
    )
    recruiter_alert = models.CharField(max_length=50, blank=True, null=True)
    first_name = models.CharField(max_length=255, blank=True, null=True, unique=True)
    last_name = models.CharField(max_length=255, blank=True, null=True, unique=True)
    email = models.CharField(max_length=50, blank=True, null=True)
    persona = models.ForeignKey(
        PersonaModel,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        default=1,
    )
    role = models.IntegerField(blank=True, null=True)
    screening_mode = models.ForeignKey(
        ScreeningModeModel,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
    )
    dob = models.DateField(blank=True, null=True)
    gender = models.ForeignKey(
        GenderModel, on_delete=models.SET_NULL, blank=True, null=True
    )
    marital_status = models.ForeignKey(
        MaritalStatusModel,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
    )
    contact_no_primary = models.IntegerField(
        blank=True, null=True
    )
    contact_no_alternate = models.IntegerField(
        blank=True, null=True
    )
    referred_by = models.ForeignKey(
        EmployeeDirectoryModel,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
    )
    referred_by_other = models.CharField(max_length=250, blank=True, null=True)
    address_line = models.CharField(max_length=255, blank=True, null=True)
    city = models.ForeignKey(
        CityModel, on_delete=models.SET_NULL, db_column="city", blank=True, null=True
    )
    pincode = models.IntegerField(blank=True, null=True)
    experience_level = models.ForeignKey(
        ExperienceLevelModel,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
    )
    education_qualification = models.ForeignKey(
        EducationQualificationModel,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
    )
    education_specialization = models.ForeignKey(
        EducationSpecializationModel,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
    )
    education_specialization_other = models.TextField(blank=True, null=True)
    education_institution = models.ForeignKey(
        EducationInstitutionModel,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
    )
    education_institution_other = models.TextField(blank=True, null=True)
    source = models.ForeignKey(
        SourceModel,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        related_name="source_for_candidate_details",
    )
    source_type = models.ForeignKey(
        SourceTypeModel,
        on_delete=models.SET_NULL,
        db_column="source_type",
        blank=True,
        null=True,
    )
    years_of_experience = models.PositiveIntegerField(
       blank=True, null=True
    )
    current_employer = models.CharField(max_length=100, blank=True, null=True)
    current_designation = models.TextField(blank=True, null=True)
    current_monthly_salary = models.IntegerField(blank=True, null=True)
    expected_monthly_salary = models.IntegerField(blank=True, null=True)
    notice_period = models.CharField(max_length=50, blank=True, null=True)
    reason_for_change = models.ForeignKey(
        ReasonForChangeModel,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
    )
    photo_path = models.TextField(blank=True, null=True)
    resume_path = models.TextField(blank=True, null=True)
    login_time = models.DateTimeField(blank=True, null=True)
    logout_time = models.DateTimeField(blank=True, null=True)
    ip_address = models.CharField(max_length=15, blank=True, null=True)
    geo_location = models.CharField(max_length=50, blank=True, null=True)
    created_date = models.DateTimeField(blank=True, null=True)
    created_by = models.IntegerField(blank=True, null=True)
    modified_date = models.DateTimeField(blank=True, null=True)
    modified_by = models.IntegerField(blank=True, null=True)
    status = models.IntegerField(default=1)

    def __str__(self):
        return str(self.first_name)

    class Meta:
        db_table = "candidate_directory"
        # constraints = [
        #     models.UniqueConstraint(
        #         fields=["first_name", "last_name"], name="full_name"
        #     )
        # ]
