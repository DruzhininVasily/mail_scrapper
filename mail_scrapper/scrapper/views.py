from rest_framework import generics
from .models import Participants
from .serializers import ParticipantsSerializer


class ParticipantsList(generics.ListCreateAPIView):
    queryset = Participants.objects.all()
    serializer_class = ParticipantsSerializer


class ParticipantsDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Participants.objects.all()
    serializer_class = Participants