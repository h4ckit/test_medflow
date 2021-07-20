from django.db import models


class DeltaTime(models.Model):
    WEEKDAYS = [
        (1, 'Monday'),
        (2, "Tuesday"),
        (3, "Wednesday"),
        (4, "Thursday"),
        (5, "Friday"),
        (6, "Saturday"),
        (7, "Sunday"),
    ]

    time_from = models.TimeField()
    time_to = models.TimeField()
    weekday = models.IntegerField(choices=WEEKDAYS)

    class Meta:
        db_table = 'delta_time'
        verbose_name = 'Время работы'
        verbose_name_plural = 'Времена работы'
