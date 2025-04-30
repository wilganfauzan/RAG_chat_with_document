from django.db import models

from core.models import BaseModel

DOC_STATUS_PENDING = "pending"
DOC_STATUS_PROCESSING = "processing"
DOC_STATUS_COMPLETE = "complete"

DOC_STATUS_CHOICES = (
    (DOC_STATUS_PENDING, "Pending"),
    (DOC_STATUS_PROCESSING, "Processing"),
    (DOC_STATUS_COMPLETE, "Complete"),
)


class Document(BaseModel):
    name = models.CharField(max_length=255, blank=True, null=True)
    file = models.FileField(upload_to="documents/")

    raw_text = models.TextField(null=True, blank=True)
    summary = models.TextField(null=True, blank=True)
    status = models.CharField(
        max_length=255, choices=DOC_STATUS_CHOICES, default=DOC_STATUS_PENDING
    )
