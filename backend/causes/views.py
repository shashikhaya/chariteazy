from django.db import IntegrityError
from rest_framework import viewsets

from .models import Cause, Vote
from .serializers import CauseSerializer, VoteSerializer


class CauseViewSet(viewsets.ModelViewSet):
    queryset = Cause.objects.all()
    serializer_class = CauseSerializer


class VoteViewSet(viewsets.ModelViewSet):
    serializer_class = VoteSerializer
    queryset = Vote.objects.all()

    def get_queryset(self):
        cause = Cause.objects.get(pk=self.kwargs["cause_pk"])
        votes = Vote.objects.filter(cause=cause)
        return votes

    def perform_create(self, serializer):
        cause = Cause.objects.get(pk=self.kwargs["cause_pk"])
        try:
            serializer.save(user=self.request.user, cause=cause)
        except IntegrityError as err:
            raise IntegrityError("You have already voted for this project")
