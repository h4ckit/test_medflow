from . import UserManager
from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    username = None

    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female')
    ]

    first_name = models.CharField(max_length=255)
    second_name = models.CharField(max_length=255, blank=True)
    last_name = models.CharField(max_length=255)

    gender = models.CharField(choices=GENDER_CHOICES, max_length=1, default='M')
    dob = models.DateField(blank=True, null=True)

    email = models.EmailField(unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']

    objects = UserManager()

    def __str__(self):
        return f"{self.email}: {self.first_name} {self.second_name}{' ' if self.second_name else ''}{self.last_name}"

    class Meta:
        db_table = 'user'
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

