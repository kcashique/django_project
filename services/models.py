from django.db import models
from versatileimagefield.fields import VersatileImageField
from django.urls import reverse_lazy
from core.models import BaseModel


class Category(BaseModel):
    title = models.CharField(max_length=128)
    title_ar = models.CharField(max_length=128)
    priority = models.PositiveIntegerField()
    icon = VersatileImageField(upload_to="categories/icons")
    featured_image = VersatileImageField(upload_to="categories/featured_images")
    description = models.TextField()
    description_ar = models.TextField()

    class Meta:
        ordering = ('-priority',)
        verbose_name = "Category"
        verbose_name_plural = "Categories"

    def __str__(self):
        return str(self.title)

    def get_services(self):
        return Service.objects.filter(is_active=True,category=self)

    def get_absolute_url(self):
        return reverse_lazy('services:category_detail', kwargs={'pk': self.pk})

    def get_update_url(self):
        return reverse_lazy('services:category_update', kwargs={'pk': self.pk})

    def get_delete_url(self):
        return reverse_lazy('services:category_delete', kwargs={'pk': self.pk})

    def get_fields(self):
        return [(field.verbose_name.title(), field.value_to_string(self)) for field in self._meta.fields]


class Service(BaseModel):
    COST_TYPE_CHOICES = (("HOURLY","HOURLY"),("PER_DAY","PER_DAY"),("PER_WORK","PER_WORK"))

    category = models.ForeignKey(
        Category, limit_choices_to={"is_active": True}, on_delete=models.PROTECT
    )
    title = models.CharField(max_length=128)
    title_ar = models.CharField(max_length=128)
    subtitle = models.CharField(max_length=128)
    subtitle_ar = models.CharField(max_length=128)
    icon = VersatileImageField(upload_to="services/icons")
    featured_image = VersatileImageField(upload_to="services/featured_images")
    description = models.TextField()
    description_ar = models.TextField()
    cost_type = models.CharField(max_length=128,choices=COST_TYPE_CHOICES)
    base_price = models.DecimalField(max_digits=128,decimal_places=2)

    class Meta:
        verbose_name = "Service"
        verbose_name_plural = "Services"

    def __str__(self):
        return str(self.title)

    def get_absolute_url(self):
        return reverse_lazy('services:service_detail', kwargs={'pk': self.pk})

    def get_update_url(self):
        return reverse_lazy('services:service_update', kwargs={'pk': self.pk})

    def get_delete_url(self):
        return reverse_lazy('services:service_delete', kwargs={'pk': self.pk})

    def get_fields(self):
        return [(field.verbose_name.title(), field.value_to_string(self)) for field in self._meta.fields]
