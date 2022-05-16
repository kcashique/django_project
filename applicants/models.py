from django.db import models
from django.urls import reverse_lazy
from core.models import BaseModel
from versatileimagefield.fields import VersatileImageField


class Applicant(BaseModel):
    name = models.CharField(max_length=128)
    email = models.EmailField()
    phone = models.CharField(max_length=128)
    password = models.CharField(max_length=30)
    image = VersatileImageField(upload_to="applicant/prof_image")
    resume = models.FileField(upload_to="applicant/resumes")

    class Meta:
        verbose_name = "Applicant"
        verbose_name_plural = "Applicants"

        def __str__(self):
            return str(self.name)


class JobApplicantion(BaseModel):
    name = models.CharField(max_length=128)
    email = models.EmailField()
    phone = models.CharField(max_length=128)
    password = models.CharField(max_length=30)
    image = VersatileImageField(upload_to="profile/prof_image")
    resume = models.FileField(upload_to="profile/resumes")

    class Meta:
        verbose_name = "JobApplicantion"
        verbose_name_plural = "JobApplicantions"

        def __str__(self):
            return str(self.name)
