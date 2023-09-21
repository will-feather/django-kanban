from django.conf import settings
from django.db import models
from django.utils import timezone


class Kanban(models.Model):
    data = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.data

    class Meta:
        db_table = "app_kanban_data"