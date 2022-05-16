import uuid

from django.db import models
from django.urls import reverse_lazy
from core.choices import NATIONALITY_CHOICES




class BaseModel(models.Model):
    id = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False, blank=True
    )
    created = models.DateTimeField(db_index=True, auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        abstract = True


class Area(BaseModel):
    title = models.CharField(max_length=128)

    def __str__(self):
        return str(self.title)


class Country(BaseModel):
    name = models.CharField(max_length=128, choices=NATIONALITY_CHOICES, default="Indian")

    class Meta:
        verbose_name = "Country"
        verbose_name_plural = "Countries"

        def __str__(self):
            return str(self.name)

    def get_absolute_url(self):
        return reverse_lazy('core:country_detail', kwargs={'pk': self.pk})

    def get_update_url(self):
        return reverse_lazy('core:country_update', kwargs={'pk': self.pk})

    def get_delete_url(self):
        return reverse_lazy('core:country_delete', kwargs={'pk': self.pk})

    def get_fields(self):
        return [
        (
            field.verbose_name.title(),
            field.value_from_object(self) if field.is_relation else field.value_from_object(self),
        )
        for field in self._meta.fields
    ]



class State(BaseModel):
    name = models.CharField(max_length=128)
    country = models.ForeignKey(Country, on_delete=models.PROTECT)

    class Meta:
        verbose_name = "State"
        verbose_name_plural = "States"

        def __str__(self):
            return str(self.name)

    def get_absolute_url(self):
        return reverse_lazy('core:state_detail', kwargs={'pk': self.pk})

    def get_update_url(self):
        return reverse_lazy('core:state_update', kwargs={'pk': self.pk})

    def get_delete_url(self):
        return reverse_lazy('core:state_delete', kwargs={'pk': self.pk})

    def get_fields(self):
        return [
        (
            field.verbose_name.title(),
            field.value_from_object(self) if field.is_relation else field.value_from_object(self),
        )
        for field in self._meta.fields
    ]


class District(BaseModel):
    name = models.CharField(max_length=128)
    state = models.ForeignKey(State, on_delete=models.PROTECT)
    country = models.ForeignKey(Country, on_delete=models.PROTECT)

    class Meta:
        verbose_name = "District"
        verbose_name_plural = "Districts"

        def __str__(self):
            return str(self.name)

    def get_absolute_url(self):
        return reverse_lazy('core:district_detail', kwargs={'pk': self.pk})

    def get_update_url(self):
        return reverse_lazy('core:district_update', kwargs={'pk': self.pk})

    def get_delete_url(self):
        return reverse_lazy('core:district_delete', kwargs={'pk': self.pk})

    def get_fields(self):
        return [
        (
            field.verbose_name.title(),
            field.value_from_object(self) if field.is_relation else field.value_from_object(self),
        )
        for field in self._meta.fields
    ]
