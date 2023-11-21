from django.core.management.base import BaseCommand
from faker import Faker
import factory
from candidates.utils import (
    EventDetailsModelFactory,
    JobRequisitionModelFactory,
    PersonaModelFactory,
    ScreeningModeModelFactory,
    GenderModelFactory,
    MaritalStatusModelFactory,
    EmployeeDirectoryModelFactory,
    CityModelFactory,
    ExperienceLevelModelFactory,
    EducationLevelModelFactory,
    EducationQualificationModelFactory,
    EducationSpecializationModelFactory,
    EducationInstitutionModelFactory,
    SourceModelFactory,
    SourceTypeModelFactory,
    ReasonForChangeModelFactory,
    CandidatedirectoryFactory,
)

fake = Faker()

class Command(BaseCommand):
    help = 'Generate fake data for the models'

    def add_arguments(self, parser):
        parser.add_argument('count', type=int, help='Number of fake entries to create')

    def handle(self, *args, **kwargs):
        count = kwargs['count']
        unique_first_names = set(fake.first_name() for _ in range(count))
        unique_last_names = set(fake.last_name() for _ in range(count))

       
        event_instances = EventDetailsModelFactory.create_batch(count)
        job_instances = JobRequisitionModelFactory.create_batch(count)
        persona_instances = PersonaModelFactory.create_batch(count)
        screening_mode_instances = ScreeningModeModelFactory.create_batch(count)
        gender_instances = GenderModelFactory.create_batch(count)
        marital_status_instances = MaritalStatusModelFactory.create_batch(count)
        employee_instances = EmployeeDirectoryModelFactory.create_batch(count)
        city_instances = CityModelFactory.create_batch(count)
        experience_level_instances = ExperienceLevelModelFactory.create_batch(count)
        education_level_instances = EducationLevelModelFactory.create_batch(count)
        education_qualification_instances = EducationQualificationModelFactory.create_batch(count)
        education_specialization_instances = EducationSpecializationModelFactory.create_batch(count)
        education_institution_instances = EducationInstitutionModelFactory.create_batch(count)
        source_instances = SourceModelFactory.create_batch(count)
        source_type_instances = SourceTypeModelFactory.create_batch(count)
        reason_for_change_instances = ReasonForChangeModelFactory.create_batch(count)
        
    
        for instances in [
            event_instances,
            job_instances,
            persona_instances,
            screening_mode_instances,
            gender_instances,
            marital_status_instances,
            employee_instances,
            city_instances,
            experience_level_instances,
            education_level_instances,
            education_qualification_instances,
            education_specialization_instances,
            education_institution_instances,
            source_instances,
            source_type_instances,
            reason_for_change_instances,
        ]:
            for instance in instances:
                instance.save()

      
        candidate_instances = CandidatedirectoryFactory.create_batch(
            count, 
            event=factory.Iterator(event_instances),
            job_position=factory.Iterator(job_instances),
            first_name=factory.Iterator(unique_first_names),
            last_name=factory.Iterator(unique_last_names),
            persona=factory.Iterator(persona_instances),
            screening_mode=factory.Iterator(screening_mode_instances),
            gender=factory.Iterator(gender_instances),
            marital_status=factory.Iterator(marital_status_instances),
            referred_by=factory.Iterator(employee_instances),
            city=factory.Iterator(city_instances),
            experience_level=factory.Iterator(experience_level_instances),
            education_qualification=factory.Iterator(education_qualification_instances),
            education_specialization=factory.Iterator(education_specialization_instances),
            education_institution=factory.Iterator(education_institution_instances),
            source=factory.Iterator(source_instances),
            source_type=factory.Iterator(source_type_instances),
            reason_for_change=factory.Iterator(reason_for_change_instances),
        )

     
        for instance in candidate_instances:
            instance.save()

        self.stdout.write(self.style.SUCCESS(f'Successfully generated {count} fake entries for all models'))
