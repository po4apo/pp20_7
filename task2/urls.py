from django.urls import path
from task2.views import show_employees

urlpatterns = [
    path('', show_employees)
]