from django.urls import path

from .views import TestView

app_name = 'medflow'
urlpatterns = [
    path('test/', TestView.as_view({'get': 'retrieve'})),
]
