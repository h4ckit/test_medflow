from rest_framework import serializers
from .models import User, Doctor


class UserCreateSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    email = serializers.EmailField()
    first_name = serializers.CharField(max_length=255)
    second_name = serializers.CharField(max_length=255, required=False, allow_null=True)
    last_name = serializers.CharField(max_length=255)
    gender = serializers.ChoiceField(choices=User.GENDER_CHOICES, required=False)
    dob = serializers.DateField(required=False, allow_null=True)
    is_doctor = serializers.BooleanField(default=False, required=False)
    is_staff = serializers.BooleanField(default=False, required=False)

    def create(self, validated_data):
        is_doctor = validated_data.pop('is_doctor')
        if is_doctor:
            instance = Doctor.objects.create(**validated_data)
        else:
            instance = User.objects.create(**validated_data)
        return instance


class UserChangeSerializer(serializers.Serializer):
    email = serializers.EmailField(required=False)
    first_name = serializers.CharField(max_length=255, required=False)
    second_name = serializers.CharField(max_length=255, required=False, allow_null=True)
    last_name = serializers.CharField(max_length=255, required=False)
    gender = serializers.ChoiceField(choices=User.GENDER_CHOICES, required=False, allow_null=True)
    dob = serializers.DateField(required=False, allow_null=True)

    def update(self, instance, validated_data):
        for field, value in validated_data.items():
            setattr(instance, field, value)
        instance.save()
        return instance


class TimeTableSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    start_time = serializers.DateTimeField()
    stop_time = serializers.DateTimeField()


class LoginSerializer(serializers.Serializer):
    email = serializers.CharField()
    password = serializers.CharField()


class StatisticsSerializer(serializers.Serializer):
    date = serializers.DateField(source='start_time__date')
    count = serializers.IntegerField(source='total')
