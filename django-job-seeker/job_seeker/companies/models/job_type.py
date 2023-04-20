from django.db import models

from common.models import Base


class JobType(Base):
    """
    It could be something like:
    * Software Development
    * Staff Augmentation
    * Head Hunting
    * Consultancy
    """
    name = models.CharField(max_length=30)

    def __str__(self) -> str:
        return self.name
