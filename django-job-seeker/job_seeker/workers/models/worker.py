from django.db import models

from common.models import Base


# Create your models here.


class Worker(Base):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    linkedin_id = models.CharField(max_length=50)
    country = models.CharField(max_length=30)

    class Meta:
        ordering = ["first_name", "last_name"]
        verbose_name_plural = "workers"

    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name}"
