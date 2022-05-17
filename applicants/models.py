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
    # resume = models.FileField(upload_to="applicant/resumes")

    class Meta:
        verbose_name = "Applicant"
        verbose_name_plural = "Applicants"

        def __str__(self):
            return str(self.name)

    def get_absolute_url(self):
        return reverse_lazy('applicants:applicant_detail', kwargs={'pk': self.pk})

    def get_update_url(self):
        return reverse_lazy('applicants:applicant_update', kwargs={'pk': self.pk})

    def get_delete_url(self):
        return reverse_lazy('applicants:applicant_delete', kwargs={'pk': self.pk})

    def get_fields(self):
        return [
        (
            field.verbose_name.title(),
            field.value_from_object(self) if field.is_relation else field.value_from_object(self),
        )
        for field in self._meta.fields
    ]


class JobApplication(BaseModel):
    name = models.CharField(max_length=128)
    email = models.EmailField()
    address = models.TextField()
    subject = models.CharField(max_length=128)
    about = models.TextField()
    skill = models.CharField(max_length=128)
    sign = VersatileImageField(upload_to="jobapplication/signature")
    resume = models.FileField(upload_to="jobapplication/resumes")

    class Meta:
        verbose_name = "JobApplicantion"
        verbose_name_plural = "JobApplicantions"

        def __str__(self):
            return str(self.name)

    def get_absolute_url(self):
        return reverse_lazy('applicants:jobapplicant_detail', kwargs={'pk': self.pk})

    def get_update_url(self):
        return reverse_lazy('applicants:jobapplicant_update', kwargs={'pk': self.pk})

    def get_delete_url(self):
        return reverse_lazy('applicants:jobapplicant_delete', kwargs={'pk': self.pk})

    def get_fields(self):
        return [
        (
            field.verbose_name.title(),
            field.value_from_object(self) if field.is_relation else field.value_from_object(self),
        )
        for field in self._meta.fields
    ]
