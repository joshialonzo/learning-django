from django.db import models

from common.models import Base


# Create your models here.


class Question(Base):
    text = models.TextField()
    answer = models.TextField(blank=True)

    class Meta:
        ordering = ["text"]
        verbose_name_plural = "questions"

    def __str__(self) -> str:
        return self.text
