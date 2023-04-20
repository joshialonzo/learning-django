from django.db import models

from common.models import Base
from .job_type import JobType

# Create your models here.


class Company(Base):
    name = models.CharField(max_length=30)
    company_url = models.URLField(max_length=400)
    linkedin_id = models.CharField(max_length=30)
    country = models.CharField(max_length=30)
    company_roles = models.ManyToManyField(JobType)

    class Meta:
        ordering = ["name"]
        verbose_name_plural = "companies"

    def __str__(self) -> str:
        return self.name
