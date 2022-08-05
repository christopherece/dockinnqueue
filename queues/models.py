from django.db import models
import uuid
from datetime import datetime

# Create your models here.


class Queue(models.Model):
    CATEGORY_TYPE = (
        ('hardware','Hardware Issue'),
        ('software','Software Issue'),
        ('phone','Phone Issue'),
        ('account','Account Issue'),

    )

    STATUS_TYPE = (
        ('Done','Done'),
        ('In Progress','In Progress'),
        ('New','New'),
    )

    name = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    type = models.CharField(max_length=200, choices=CATEGORY_TYPE)
    status = models.CharField(max_length=200, choices=STATUS_TYPE)
    ritm = models.CharField(max_length=200, blank=True, null=True)
    technician = models.CharField(max_length=200, blank=True, null=True)
    comment = models.TextField(null=True, blank=True)
    queue_id = models.IntegerField(default=0)
    is_done = models.IntegerField(default=0)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True,
                    primary_key=True, editable=False)


    def __str__(self):
        return self.name