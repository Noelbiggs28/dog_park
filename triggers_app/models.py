from django.db import models

class Triggers(models.Model):
    trigger_name = models.CharField(max_length=255)

    def __str__(self):
        return self.trigger_name