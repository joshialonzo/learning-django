from django.db import models

from companies.models.company import Company


class SoftwareCompany(Company):
    COMPANY_TYPE_CHOICES = [
        ("StartUp", "StartUp"),
        ("Factory", "Factory"),
        ("Enterprise", "Enterprise"),
    ]

    INDUSTRY_CHOICES = [
        ("Software", "Software"),
        ("Education", "Education"),
        ("Energy", "Energy"),
        ("Manufacturing", "Manufacturing"),
        ("Finance", "Finance"),
        ("Social Media", "Social Media"),
        ("Media", "Media"),
    ]

    software_company_type = models.CharField(
        max_length=20,
        choices=COMPANY_TYPE_CHOICES,
        default="Enterprise",
    )
    industry = models.CharField(
        max_length=20,
        choices=INDUSTRY_CHOICES,
        default="Software",
    )

    class Meta:
        ordering = ["name"]
        verbose_name_plural = "Software companies"
