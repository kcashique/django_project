from django.db import models
from django.urls import reverse_lazy
from core.models import BaseModel
from versatileimagefield.fields import VersatileImageField


# Create your models here.
class Recruiter(BaseModel):
    name = models.CharField(max_length=128)
    role = models.CharField(max_length=128)
    skill = models.CharField(max_length=128)
    phone = models.CharField(max_length=128)
    date_of_birth = models.DateField()

    class Meta:
        verbose_name = "Applicant"
        verbose_name_plural = "Applicants"

        def __str__(self):
            return str(self.name)

    def get_absolute_url(self):
        return reverse_lazy('recruiters:recreruit_detail', kwargs={'pk': self.pk})

    def get_update_url(self):
        return reverse_lazy('recruiters:recreruit_update', kwargs={'pk': self.pk})

    def get_delete_url(self):
        return reverse_lazy('recruiters:recreruit_delete', kwargs={'pk': self.pk})

    def get_fields(self):
        return [
        (
            field.verbose_name.title(),
            field.value_from_object(self) if field.is_relation else field.value_from_object(self),
        )
        for field in self._meta.fields
    ]
