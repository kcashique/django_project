from django.db import models
from core.models import BaseModel
from django.urls import reverse_lazy
from core.choices import NATIONALITY_CHOICES, PASSOUT_CHOICES, ROLE_CHOICES
from versatileimagefield.fields import VersatileImageField



class Country(BaseModel):
    name = models.CharField(max_length=128)

    class Meta:
        verbose_name = "Country"
        verbose_name_plural = "Countris"

        def __str__(self):
            return str(self.name)


class State(BaseModel):
    name = models.CharField(max_length=128)
    country = models.ForeignKey(Country, on_delete=models.PROTECT)

    class Meta:
        verbose_name = "State"
        verbose_name_plural = "States"

        def __str__(self):
            return str(self.name)


class Company(BaseModel):
    name = models.CharField(max_length=128)
    logo = VersatileImageField(upload_to="company/logo")
    location = models.CharField(max_length=128)
    industry = models.CharField(max_length=128)

    class Meta:
        verbose_name = "Company"
        verbose_name_plural = "Companys"

        def __str__(self):
            return str(self.name)


class Job(BaseModel):
    job_title = models.CharField(max_length=128)
    job_name = models.CharField(max_length=128)
    company = models.CharField(max_length=128)
    job_requirment = models.CharField(max_length=128)
    salary = models.CharField(max_length=128)
    job_location = models.ForeignKey(State, related_name="applied_state", on_delete=models.CASCADE)
    job_description = models.TextField()


    class Meta:
        verbose_name = "Job"
        verbose_name_plural = "Jobs"

    def __str__(self):
        return str(self.job_name)

    def get_absolute_url(self):
        return reverse_lazy('jobs:job_detail', kwargs={'pk': self.pk})

    def get_update_url(self):
        return reverse_lazy('jobs:job_update', kwargs={'pk': self.pk})

    def get_delete_url(self):
        return reverse_lazy('jobs:job_delete', kwargs={'pk': self.pk})

    def get_fields(self):
        return [
        (
            field.verbose_name.title(),
            field.value_from_object(self) if field.is_relation else field.value_from_object(self),
        )
        for field in self._meta.fields
    ]


class profile(BaseModel):
    name = models.CharField(max_length=128)
    address = models.TextField()
    image = VersatileImageField(upload_to="profile/prof_image")
    resume =

    class Meta:
        verbose_name = "Profile"
        verbose_name_plural = "Profiles"

        def __str__(self):
            return str(self.name)
    # [(x,x-1) for x in [1,2]]
