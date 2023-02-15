from django.db import models


class SalesOrder(models.Model):
    name = models.CharField(max_length=255, blank=False, default='before')
    amount = models.IntegerField()
    description = models.CharField(max_length=255)

    def __str__(self):
        return self.name
