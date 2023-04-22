from django.db import models

from common.models import Base
from companies.models.headhunting import HeadhuntingFirm
from jobs.models.job_description import JobDescription


# Create your models here.


class SelectionProcess(Base):
    STATUS_CHOICES = [
        (0, "Zero"),
        (1, "Started"),
        (2, "Waiting"),
        (3, "Rejected"),
        (4, "Offer"),
        (5, "Accepted"),
    ]

    job_description = models.ForeignKey(
        JobDescription,
        on_delete=models.CASCADE,
    )
    headhunting_firm = models.ForeignKey(
        HeadhuntingFirm,
        on_delete=models.CASCADE,
    )
    status = models.IntegerField(
        choices=STATUS_CHOICES,
        default="Zero"
    )

    class Meta:
        ordering = ["job_description", "status"]
        verbose_name_plural = "Selection processes"

    def __str__(self) -> str:
        return (
            f"Description: {self.job_description} "
            f"Status: {self.status}"
        )
