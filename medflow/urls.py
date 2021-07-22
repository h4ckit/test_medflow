from django.urls import path

from medflow.views import UserView, TimeTableView, LoginView, TimeTableStatsView

app_name = 'medflow'
urlpatterns = [
    path('login/', LoginView.as_view({'post': 'login'})),
    path('user/<user_id>/', UserView.as_view({'put': 'partial_update', 'delete': 'destroy'})),
    path('user/', UserView.as_view({'post': 'create'})),
    path('doctor/timetable/<doctor_id>/', TimeTableView.as_view({'get': 'list'})),
    path('timetable/<timetable_id>/', TimeTableView.as_view({'put': 'partial_update', 'delete': 'destroy'})),
    path('statistics/', TimeTableStatsView.as_view({'get': 'list'})),
]
