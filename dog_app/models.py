from django.db import models
from triggers_app.models import Triggers
from owner_app.models import Owner



class Dog(models.Model):
    dog_name = models.CharField(max_length=120)
    age = models.IntegerField()
    triggers = models.ManyToManyField(Triggers)
    owner = models.ForeignKey(Owner,default=1, on_delete=models.CASCADE)
    description = models.TextField()


    def __str__(self):
        return self.dog_name
    
    def add_trigger(self, trigger):
        self.triggers.add(trigger)

    def remove_trigger(self, trigger):
        self.triggers.remove(trigger)

    def change_owner(self, owner):
        self.owner = owner