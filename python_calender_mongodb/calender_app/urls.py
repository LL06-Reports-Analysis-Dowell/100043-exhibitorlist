from django.urls import path
from . import views

app_name = 'calendar_app'

urlpatterns = [
    # path('', views.index, name='main-view'),
    path('', views.CalendarView.as_view(), name='calendars'),
    path('<str:filter_date>/', views.FilterCalendarView.as_view(), name='filter-calendar'),
]
