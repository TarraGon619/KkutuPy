from django.urls import path
from . import views

app_name = 'main'

urlpatterns = [
    path('', views.lobby, name='lobby'),
    path('room/<int:room_id>/', views.room, name='room')
]
