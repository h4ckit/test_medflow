from django.db import models


class TimeTable(models.Model):
    doctor = models.ForeignKey('Doctor', on_delete=models.CASCADE, related_name='doctor_time_tables')
    client = models.ForeignKey('User', on_delete=models.SET_NULL, null=True, blank=True,
                               related_name='user_time_tables')

    start_time = models.DateTimeField()
    stop_time = models.DateTimeField()

    class Meta:
        db_table = 'time_table'
        verbose_name = 'Слот врача'
        verbose_name_plural = 'Слоты врачей'
