from django.contrib import admin
from django.urls import path, include
from rest_framework.schemas import get_schema_view

SCHEMA_NAME = "api-schema"

api_v1_patterns = [
    path('', include('agency_app.urls')),
]

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(api_v1_patterns)),
    path('schema-api/', get_schema_view(
        title="Rec API Scheme",
        description="API for all things … and other",
        version="0.0.0"
    ), name=SCHEMA_NAME),
]