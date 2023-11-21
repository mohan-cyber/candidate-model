import factory
from faker import Faker
from .models import (
    EventDetailsModel,
    JobRequisitionModel,
    PersonaModel,
    ScreeningModeModel,
    GenderModel,
    MaritalStatusModel,
    EmployeeDirectoryModel,
    CityModel,
    ExperienceLevelModel,
    EducationLevelModel,
    EducationQualificationModel,
    EducationSpecializationModel,
    EducationInstitutionModel,
    SourceModel,
    SourceTypeModel,
    ReasonForChangeModel,
    Candidatedirectory,
)

fake = Faker()

class EventDetailsModelFactory(factory.Factory):
    class Meta:
        model = EventDetailsModel

    name = fake.word()
    date = fake.date()
    description = fake.text()

class JobRequisitionModelFactory(factory.Factory):
    class Meta:
        model = JobRequisitionModel

    title = fake.word()
    department = fake.word()
    description = fake.text()

class PersonaModelFactory(factory.Factory):
    class Meta:
        model = PersonaModel

    name = fake.word()
    description = fake.text()

class ScreeningModeModelFactory(factory.Factory):
    class Meta:
        model = ScreeningModeModel

    name = fake.word()
    description = fake.text()

class GenderModelFactory(factory.Factory):
    class Meta:
        model = GenderModel

    name = fake.word()

class MaritalStatusModelFactory(factory.Factory):
    class Meta:
        model = MaritalStatusModel

    status = fake.word()

class EmployeeDirectoryModelFactory(factory.Factory):
    class Meta:
        model = EmployeeDirectoryModel

    # employee_id = fake.uuid4()
    first_name = fake.first_name()
    last_name = fake.last_name()
    email = fake.email()

class CityModelFactory(factory.Factory):
    class Meta:
        model = CityModel

    name = fake.city()
    country = fake.country()

class ExperienceLevelModelFactory(factory.Factory):
    class Meta:
        model = ExperienceLevelModel

    level = fake.word()
    description = fake.text()

class EducationLevelModelFactory(factory.Factory):
    class Meta:
        model = EducationLevelModel

    level = fake.word()
    description = fake.text()

class EducationQualificationModelFactory(factory.Factory):
    class Meta:
        model = EducationQualificationModel

    qualification = fake.word()
    description = fake.text()

class EducationSpecializationModelFactory(factory.Factory):
    class Meta:
        model = EducationSpecializationModel

    specialization = fake.word()
    description = fake.text()

class EducationInstitutionModelFactory(factory.Factory):
    class Meta:
        model = EducationInstitutionModel

    education_institution = fake.word()
    description = fake.text()

class SourceModelFactory(factory.Factory):
    class Meta:
        model = SourceModel

    name = fake.word()
    description = fake.text()

class SourceTypeModelFactory(factory.Factory):
    class Meta:
        model = SourceTypeModel

    name = fake.word()
    description = fake.text()

class ReasonForChangeModelFactory(factory.Factory):
    class Meta:
        model = ReasonForChangeModel

    reason = fake.word()
    description = fake.text()

class CandidatedirectoryFactory(factory.Factory):
    class Meta:
        model = Candidatedirectory

    event = factory.SubFactory(EventDetailsModelFactory)
    job_position = factory.SubFactory(JobRequisitionModelFactory)
    recruiter_alert = fake.word()
    first_name = fake.first_name()
    last_name = fake.last_name()
    email = fake.email()
    persona = factory.SubFactory(PersonaModelFactory)
    role = fake.random_int()
    screening_mode = factory.SubFactory(ScreeningModeModelFactory)
    dob = fake.date_of_birth()
    gender = factory.SubFactory(GenderModelFactory)
    marital_status = factory.SubFactory(MaritalStatusModelFactory)
    contact_no_primary = fake.random_number(digits=10)
    contact_no_alternate = fake.random_number(digits=10)
    referred_by = factory.SubFactory(EmployeeDirectoryModelFactory)
    referred_by_other = fake.word()
    address_line = fake.address()
    city = factory.SubFactory(CityModelFactory)
    pincode = fake.random_number(digits=6)
    experience_level = factory.SubFactory(ExperienceLevelModelFactory)
    education_qualification = factory.SubFactory(EducationQualificationModelFactory)
    education_specialization = factory.SubFactory(EducationSpecializationModelFactory)
    education_specialization_other = fake.text()
    education_institution = factory.SubFactory(EducationInstitutionModelFactory)
    education_institution_other = fake.text()
    source = factory.SubFactory(SourceModelFactory)
    source_type = factory.SubFactory(SourceTypeModelFactory)
    years_of_experience = fake.random_number(digits=4)
    current_employer = fake.company()
    current_designation = fake.text()
    current_monthly_salary = fake.random_int()
    expected_monthly_salary = fake.random_int()
    notice_period = fake.word()
    reason_for_change = factory.SubFactory(ReasonForChangeModelFactory)
    photo_path = fake.image_url()
    resume_path = fake.file_path()
    login_time = fake.date_time_this_year()
    logout_time = fake.date_time_this_year()
