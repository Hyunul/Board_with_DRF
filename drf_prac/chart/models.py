# your_app_name/models.py
from django.db import models

class DataPoint(models.Model):
    value = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"DataPoint(value={self.value}, created_at={self.created_at})"
