from django.db import models

# Create your models here.

class Event(models.Model):
    name = models.CharField(max_length=100, unique=True)
    datetime = models.DateTimeField(null=False)

    def __str__(self) -> str:
        return self.name + " taking place on " + str(self.datetime)

class Invite(models.Model):
    names = models.CharField(max_length=200)
    replied = models.BooleanField(default=False)
    invitedNum = models.IntegerField(default=1)
    confirmedNum = models.IntegerField(default=0)
    allergies = models.CharField(null=True, max_length=200)
    requestedSong = models.CharField(null=True, max_length=200)
    event = models.ForeignKey(to=Event, on_delete=models.CASCADE, null=False)

    def __str__(self) -> str:
        return self.names
