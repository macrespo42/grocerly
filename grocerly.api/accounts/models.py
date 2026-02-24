from django.db.models.fields import DateTimeField
from django.db.models.fields.related import ForeignKey
from django.contrib.gis.db.models import CharField
from django.db import models
from django.contrib.auth.models import AbstractUser


class Family(models.Model):
    name: CharField = models.CharField(max_length=42)
    created_at: DateTimeField = models.DateTimeField(auto_now_add=True)
    updated_at: DateTimeField = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.name


class User(AbstractUser):
    family: ForeignKey[Family | None] = models.ForeignKey(
        Family, on_delete=models.CASCADE, default=None, null=True, blank=True
    )
    created_at: DateTimeField = models.DateTimeField(auto_now_add=True)
    updated_at: DateTimeField = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.username
