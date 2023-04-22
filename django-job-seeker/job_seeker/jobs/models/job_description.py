from django.db import models

from companies.models.software_company import SoftwareCompany
from common.models import Base
from technologies.models import Technology


# Create your models here.


class JobDescription(Base):
    SCHEMA_CHOICES = [
        ("Payroll", "Payroll"),
        ("Contractor", "Contractor"),
    ]
    LOCATION_CHOICES = [
        ("Remote", "Remote"),
        ("On-site", "On-site"),
        ("Hybrid", "Hybrid"),
    ]
    STATUS_CHOICES = [
        ("Active", "Active"),
        ("Inactive", "Inactive"),
    ]

    title = models.CharField(max_length=30, blank=True)
    minimum_salary = models.IntegerField(blank=True, null=True)
    maximum_salary = models.IntegerField(blank=True, null=True)
    url = models.URLField(blank=True, null=True)
    schema = models.CharField(
        max_length=20,
        choices=SCHEMA_CHOICES,
        default="Contractor"
    )
    location = models.CharField(
        max_length=20,
        choices=LOCATION_CHOICES,
        default="Remote"
    )
    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default="Active"
    )
    description = models.TextField(blank=True)
    software_company = models.ForeignKey(
        SoftwareCompany,
        on_delete=models.CASCADE,
        blank=True,
        null=True,
    )
    technologies = models.ManyToManyField(Technology)

    class Meta:
        ordering = ["title"]
        verbose_name_plural = "Job descriptions"

    def __str__(self) -> str:
        stack = [t.name for t in self.technologies.all()]
        stack_string = ", ".join(stack)
        return f"{self.title}: {stack_string}"
