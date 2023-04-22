from django.db import models

from common.models import Base

# Create your models here.


class Technology(Base):
    name = models.CharField(max_length=30)

    class Meta:
        ordering = ["name"]
        verbose_name_plural = "technologies"

    def __str__(self) -> str:
        return self.name
