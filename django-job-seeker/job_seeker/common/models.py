import uuid
from django.db import models
from django.utils import timezone

# Create your models here.


class Base(models.Model):

    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False,
        db_comment="Primary key for all the models"
    )
    created_date = models.DateTimeField(
        db_comment="Object creation date",
        auto_now=False, auto_now_add=True,
    )
    updated_date = models.DateTimeField(
        db_comment="Object updating date",
        auto_now=True, auto_now_add=False,
    )

    class Meta:
        abstract = True
