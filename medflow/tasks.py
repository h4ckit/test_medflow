from django.apps import apps
from celery import shared_task


@shared_task
def create_time_tables():
    doctors = apps.get_model('medflow', 'Doctor').objects.all()
    print(doctors)
