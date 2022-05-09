from django.db import models
from versatileimagefield.fields import VersatileImageField

from core.models import BaseModel


class Category(BaseModel):
    title = models.CharField(max_length=128)
    priority = models.PositiveIntegerField()
    icon = VersatileImageField(upload_to="categories/icons")
    featured_image = VersatileImageField(upload_to="categories/featured_images")
    description = models.TextField()

    def __str__(self):
        return str(self.title)

    def get_services(self):
        return Service.objects.filter(is_active=True,category=self)

    class Meta:
        ordering = ('-priority',)
        verbose_name = "Category"
        verbose_name_plural = "Categories"


class Service(BaseModel):
    COST_TYPE_CHOICES = (("HOURLY","HOURLY"),("PER_DAY","PER_DAY"),("PER_WORK","PER_WORK"))

    category = models.ForeignKey(
        Category, limit_choices_to={"is_active": True}, on_delete=models.PROTECT
    )
    title = models.CharField(max_length=128)
    subtitle = models.CharField(max_length=128)
    icon = VersatileImageField(upload_to="services/icons")
    featured_image = VersatileImageField(upload_to="services/featured_images")
    description = models.TextField()
    cost_type = models.CharField(max_length=128,choices=COST_TYPE_CHOICES)
    base_price = models.DecimalField(max_digits=128,decimal_places=2)

    def __str__(self):
        return str(self.title)

    class Meta:
        verbose_name = "Service"
        verbose_name_plural = "Services"
