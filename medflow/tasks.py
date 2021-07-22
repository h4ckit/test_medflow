from django.apps import apps
from celery import shared_task
import datetime


@shared_task
def create_time_tables():
    doctors = apps.get_model('medflow', 'Doctor').objects.all()

    for doctor in doctors:
        days_to_generate = doctor.days_to_generate  # int
        work_time = doctor.work_time  # many to many
        vacation_start = doctor.vacation_start  # date
        vacation_end = doctor.vacation_end  # date
        lunch_break = doctor.lunch_break  # manytomany
        slot_time = doctor.slot_time  # time field

        time_tables = doctor.doctor_time_tables.all()
        time_tables = time_tables.filter(start_time__date__gte=datetime.date.today())
        for day in range(1, days_to_generate):
            current_day = datetime.date.today() + datetime.timedelta(days=day)
            current_time_tables = time_tables.filter(start_time__date=current_day)
            if current_time_tables.count():
                continue
            # need to generate

            # check vacation
            if vacation_start and vacation_end:
                if vacation_start.date() <= current_day <= vacation_end.date():
                    continue

            current_work_time = work_time.filter(weekday=current_day.weekday()).first()
            if not current_work_time:
                continue
            current_lunch_time = lunch_break.filter(weekday=current_day.weekday()).first()
            generates = []
            if current_lunch_time:
                # before_lunch
                generates.append([current_work_time.time_from, current_lunch_time.time_from])
                # after_lunch
                generates.append([current_lunch_time.time_to, current_work_time.time_to])
            else:
                generates.append([current_work_time.time_from, current_work_time.time_to])

            for data in generates:
                time_from, time_to = data
                duration_minutes = int(datetime.timedelta(hours=slot_time.hour,
                                                          minutes=slot_time.minute).total_seconds() / 60)

                total_minutes = int((datetime.datetime.combine(datetime.date.today(), time_to) -
                                     datetime.datetime.combine(datetime.date.today(), time_from)).total_seconds() / 60)
                for i in range(total_minutes // duration_minutes):
                    start_time = datetime.datetime.combine(current_day, time_from) + datetime.timedelta(
                        minutes=duration_minutes * i)
                    stop_time = datetime.datetime.combine(current_day, time_from) + datetime.timedelta(
                        minutes=duration_minutes * (i + 1))

                    apps.get_model('medflow', 'TimeTable').objects.create(doctor=doctor,
                                                                          start_time=start_time,
                                                                          stop_time=stop_time)
