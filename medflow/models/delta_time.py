from django.db import models


class DeltaTime(models.Model):
    WEEKDAYS = [
        (0, 'Monday'),
        (1, "Tuesday"),
        (2, "Wednesday"),
        (3, "Thursday"),
        (4, "Friday"),
        (5, "Saturday"),
        (6, "Sunday"),
    ]

    time_from = models.TimeField()
    time_to = models.TimeField()
    weekday = models.IntegerField(choices=WEEKDAYS)

    class Meta:
        db_table = 'delta_time'
        verbose_name = 'Время работы'
        verbose_name_plural = 'Времена работы'
