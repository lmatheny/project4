from django.urls import path
from django.http import HttpResponse
from .views import home_view
from .views import person_view
from .views import stopwatch_view
from .views import newDay_view
from .views import success_page_view
from .views import calendar_view
from .views import login_view



urlpatterns = [
    path('', login_view, name='login'),
    path('home.html', home_view, name='home'),
    path('person.html', person_view, name='person'),
    path('stopwatch.html', stopwatch_view, name='stopwatch'),
    path('newDay.html', newDay_view, name='new_day'),
    path('success_page/', success_page_view, name='success_page'),
    path('calendar.html', calendar_view, name='calendar_view'),
    path('login.html', login_view, name='login_view'),
]