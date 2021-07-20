from django.db import models
import datetime
from . import User


class Doctor(User):
    days_to_generate = models.IntegerField(default=7)
    work_time = models.ManyToManyField('DeltaTime', related_name='doctor_work_times')
    vacation = models.DateTimeField(blank=True)
    lunch_break = models.ManyToManyField('DeltaTime', related_name='doctor_lunch_breaks')
    slot_time = models.TimeField(default=datetime.time(0, 20, 0))

    class Meta:
        db_table = 'doctor'
        verbose_name = 'Врач'
        verbose_name_plural = 'Врачи'
