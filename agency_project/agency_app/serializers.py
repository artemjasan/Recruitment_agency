from rest_framework import serializers

from .models import Candidate, Job


class CandidateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Candidate
        fields = "__all__"


class JobListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Job
        fields = ("id", "title", "salary", "full_ad_text", "candidate",)
        read_only_fields = ("candidate",)


class DefaultJobSerializer(serializers.ModelSerializer):
    class Meta:
        model = Job
        fields = ("id", "title", "salary", "full_ad_text", "candidate",)


class JobApplySerializer(serializers.ModelSerializer):
    class Meta:
        model = Job
        fields = ("id", "title", "salary", "full_ad_text", "candidate",)
        read_only_fields = ("id", "title", "salary", "full_ad_text",)
