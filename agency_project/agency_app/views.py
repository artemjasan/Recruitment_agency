from rest_framework import status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from .models import Candidate, Job
from .serializers import CandidateSerializer, JobListSerializer, DefaultJobSerializer, JobApplySerializer


class CandidatesViewSet(ModelViewSet):
    queryset = Candidate.objects.all()
    serializer_class = CandidateSerializer


class JobsViewSet(ModelViewSet):
    queryset = Job.objects.all()
    serializer_class = DefaultJobSerializer

    action_serializers = {
        'list': JobListSerializer,
        'create': JobListSerializer,
        'apply': JobApplySerializer,
    }

    def get_serializer_class(self):

        if hasattr(self, 'action_serializers'):
            return self.action_serializers.get(self.action, self.serializer_class)

        return super(JobsViewSet, self).get_serializer_class()

    # Extra action for apply job by candidates
    @action(detail=True, methods=["post"])
    def apply(self, request, pk=None):
        job = self.get_object()
        candidate_id = request.data.get("candidate")
        if candidate_id is None or not Candidate.objects.filter(pk=candidate_id).exists() or not int:
            return Response("Please, write a valid data.", status=status.HTTP_400_BAD_REQUEST)
        candidate = Candidate.objects.get(pk=candidate_id)
        if candidate not in job.candidate.all():
            job.candidate.add(candidate)
            return Response(f"Dear {candidate}, your application was successfully added.", status=status.HTTP_200_OK)
        else:
            return Response(f"Dear {candidate}, your application already exists.", status=status.HTTP_200_OK)