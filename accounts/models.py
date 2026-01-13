from django.db import models
from django.contrib.auth.models import AbstractUser


class Family(models.Model):
    name = models.CharField(max_length=42)


class User(AbstractUser):
    family = models.ForeignKey(
        Family, on_delete=models.CASCADE, default=None, null=True, blank=True
    )

    def __str__(self) -> str:
        return self.username
