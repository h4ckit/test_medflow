from rest_framework.viewsets import ModelViewSet
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from .serializers import UserCreateSerializer, UserChangeSerializer, TimeTableSerializer, LoginSerializer, \
    StatisticsSerializer
from .models import User, TimeTable
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from django.db.models import Count


class UserView(ModelViewSet):
    serializer_class = UserCreateSerializer
    permission_classes = (IsAdminUser,)

    def get_queryset(self):
        return User.objects.all()

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        serializer.save()
        result = serializer.data

        return Response(result, status=201)

    def partial_update(self, request, user_id: int, *args, **kwargs):
        query = self.get_queryset()
        obj = get_object_or_404(query, id=user_id)

        serializer = UserChangeSerializer(obj, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        result = self.get_serializer(serializer.instance).data

        return Response(result)

    def destroy(self, request, user_id: int, *args, **kwargs):
        query = self.get_queryset()
        obj = get_object_or_404(query, id=user_id)

        obj.is_active = False
        obj.save()
        return Response(status=200)


class TimeTableView(ModelViewSet):
    serializer_class = TimeTableSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self, doctor_id):
        return TimeTable.objects.filter(doctor_id=doctor_id, client__isnull=True)

    def list(self, request, doctor_id, *args, **kwargs):
        query = self.get_queryset(doctor_id)
        serializer = self.get_serializer(query, many=True)
        result = serializer.data
        return Response(result)

    def partial_update(self, request, timetable_id, *args, **kwargs):
        obj = get_object_or_404(TimeTable, id=timetable_id)

        if obj.client:
            return Response(status='400')

        obj.client = request.user
        obj.save()
        return Response(status='200')

    def destroy(self, request, timetable_id, *args, **kwargs):
        obj = get_object_or_404(TimeTable, id=timetable_id)

        if not obj.client:
            return Response(status='400')

        obj.client = None
        obj.save()
        return Response(status='200')


class LoginView(ModelViewSet):
    serializer_class = LoginSerializer

    def login(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        email = serializer.data['email']
        password = serializer.data['password']

        user = get_object_or_404(User.objects.all(), email=email)
        if not user.check_password(password):
            return Response(status='401')
        token, status = Token.objects.get_or_create(user=user)
        result = {
            'token': token.key
        }
        return Response(result)


class TimeTableStatsView(ModelViewSet):
    serializer_class = StatisticsSerializer

    def get_queryset(self):
        query = TimeTable.objects.filter(client__isnull=True)
        query = query.values('start_time__date').annotate(total=Count('start_time__date'))
        return query

    def list(self, request, *args, **kwargs):
        query = self.get_queryset()
        serializer = self.get_serializer(query, many=True)
        result = serializer.data
        return Response(result)
