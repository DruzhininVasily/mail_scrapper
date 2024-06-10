from django.urls import path
from .views import ParticipantsList, ParticipantsDetail

urlpatterns = [
    path('participants/', ParticipantsList.as_view(), name='participants_list'),
    path('participants/<int:pk>/', ParticipantsDetail.as_view(), name='participants_detail'),
]