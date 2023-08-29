from django.db import models

class Owner(models.Model):
    owners_name= models.CharField(max_length=255)

    def __str__(self):
        return self.owners_name