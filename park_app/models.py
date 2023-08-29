from django.db import models
from dog_app.models import Dog


class DogPark(models.Model):
    dog_park_name = models.CharField(max_length=255)
    dogs = models.ManyToManyField(Dog)

    def __str__(self):
        return self.dog_park_name

    def add_dog(self, dog):
        self.dogs.add(dog)

    def remove_dog(self, dog):
        self.dogs.remove(dog)

# not implemented yet
    def view_all_triggers(self):
        triggers = set()
        for dog in self.dogs.all():
            triggers.update(dog.triggers.all())
        return triggers