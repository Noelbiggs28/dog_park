from django.db import models
from triggers_app.models import Triggers
# from owner_app.models import Owner
from user_profile.models import UserProfile


class Dog(models.Model):
    dog_name = models.CharField(max_length=120)
    age = models.IntegerField()
    triggers = models.ManyToManyField(Triggers)
    description = models.TextField()
    owner = models.ForeignKey(UserProfile, on_delete=models.CASCADE) 
    likes = models.ManyToManyField('self', symmetrical=False, blank=True)


    def __str__(self):
        return self.dog_name
    
    # def add_trigger(self, trigger_pk):
    #     trigger = Triggers.objects.get(pk=trigger_pk)
    #     self.triggers.add(trigger)

    # def remove_trigger(self, trigger_pk):
    #     trigger = Triggers.objects.get(pk=trigger_pk)
    #     self.triggers.remove(trigger)

    # def change_owner(self, owner):
    #     owner = Owner.objects.get(pk=owner)
    #     self.owner = owner

    # def add_like(self, pk):
    #     dog = Dog.objects.get(pk=pk)
    #     self.likes.add(dog)

    # def remove_like(self, pk):
    #     dog = Dog.objects.get(pk=pk)
    #     self.likes.remove(dog)