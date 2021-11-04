from django.urls import path
from . import views

app_name = 'exhibitors'

urlpatterns = [
    path('', views.index, name='main-view'),
    path('submit/1/',views.multistepform1_save, name='multistepform1'),
    path('submit/2/',views.multistepform2_save, name='multistepform2'),
    path('thanks/',views.response_recorded,name='thanks'),
    path('details/',views.event_details,name='details'),
    path('create_email/',views.create_email,name='mail'),
    path('email/',views.send_email,name='send-email'),
]
