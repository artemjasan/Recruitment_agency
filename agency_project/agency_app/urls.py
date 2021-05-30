from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import CandidatesViewSet, JobsViewSet

router = DefaultRouter()

# Router for candidate endpoints:
# http://127.0.0.1:8000/api/candidates - List view (list of candidates and creation a new candidate)
# http://127.0.0.1:8000/api/candidates/{id}/ - Detail view (retrieve/delete/update of the selected candidate)
router.register(r'candidates', CandidatesViewSet, basename='candidate')
# Router for job endpoints:
# http://127.0.0.1:8000/api/jobs - List view (list of jobs and creation a new job)
# http://127.0.0.1:8000/api/jobs/{id}/ - Detail view (retrieve/delete/update of the selected job)
# http://127.0.0.1:8000/api/jobs/{id}/apply/ - Extra action with ability to add candidate to the job
router.register(r'jobs', JobsViewSet, basename='job')

urlpatterns = [
    path("", include(router.urls))
]
