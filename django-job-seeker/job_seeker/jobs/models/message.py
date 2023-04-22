from django.db import models

from common.models import Base
from workers.models.worker import Worker

from jobs.validators import PhoneRegex


# Create your models here.


class Message(Base):
    CHANNEL_CHOICES = [
        ("LinkedIn", "LinkedIn"),
        ("Email", "Email"),
        ("WhatsApp", "WhatsApp"),
    ]
    LANGUAGE_CHOICES = [
        ("English", "English"),
        ("Spanish", "Spanish"),
    ]

    channel = models.CharField(
        max_length=20,
        choices=CHANNEL_CHOICES,
        default="LinkedIn",
    )
    language = models.CharField(
        max_length=20,
        choices=LANGUAGE_CHOICES,
        default="English",
    )
    sender = models.ForeignKey(
        Worker,
        related_name="sender",
        on_delete=models.CASCADE,
    )
    receiver = models.ForeignKey(
        Worker,
        related_name="receiver",
        on_delete=models.CASCADE,
    )
    timestamp = models.DateTimeField()
    email = models.EmailField(blank=True, null=True)
    phone = models.CharField(
        validators=[PhoneRegex],
        max_length=20,
        blank=True,
    )
    text = models.TextField()

    class Meta:
        ordering = ["timestamp"]
        verbose_name_plural = "messages"

    def __str__(self) -> str:
        if self.email:
            media = self.email
        elif self.phone:
            media = self.phone
        else:
            media = "LinkedIn"
        return (
            f"From {self.sender} "
            f"to {self.receiver} "
            f"on {str(self.timestamp)} "
            f"- {media}"
        )
