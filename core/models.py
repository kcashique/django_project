import uuid

from django.db import models


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
