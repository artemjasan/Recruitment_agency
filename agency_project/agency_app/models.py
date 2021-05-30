from django.core.validators import MinValueValidator
from django.db import models


class Candidate(models.Model):
    full_name = models.CharField(max_length=100)
    expected_salary = models.IntegerField(validators=[MinValueValidator(1000)])
    skill_list = models.CharField(max_length=255)

    def __str__(self):
        return self.full_name


class Job(models.Model):
    title = models.CharField(max_length=100)
    salary = models.IntegerField(validators=[MinValueValidator(1000)])
    full_ad_text = models.CharField(max_length=255)
    candidate = models.ManyToManyField('Candidate', related_name='candidates', blank=True)

    def __str__(self):
        return self.title

