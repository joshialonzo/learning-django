from django.db import models

from common.models import Base
from jobs.models.question import Question
from jobs.models.selection_process import SelectionProcess


# Create your models here.


class Stage(Base):
    CHANNEL_CHOICES = [
        (0, "Phone"),
        (1, "Email"),
        (2, "Meet"),
        (3, "Test"),        
    ]

    selection_process = models.ForeignKey(
        SelectionProcess,
        on_delete=models.CASCADE,
    )
    channel = models.IntegerField(
        choices=CHANNEL_CHOICES,
        default="Zero"
    )
    platform = models.CharField(
        max_length=30, blank=True,
    )
    event_date = models.DateTimeField(
        blank=True, null=True,
    )
    questions = models.ManyToManyField(Question)

    class Meta:
        ordering = ["event_date"]
        verbose_name_plural = "stages"

    def __str__(self) -> str:
        return (
            f"Process: {self.selection_process} "
            f"Channel: {self.channel} "
            f"Date: {self.event_date}"
        )
