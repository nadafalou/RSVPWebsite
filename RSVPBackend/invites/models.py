from django.db import models

# Create your models here.

class Guest(models.Model):
    names = models.CharField(max_length=200)
    replied = models.BooleanField(default=False)
    invitedNum = models.IntegerField(default=1)
    confirmedNum = models.IntegerField(default=0)
    allergies = models.CharField(null=True, max_length=200)
    requestedSong = models.CharField(null=True, max_length=200)

    def __str__(self) -> str:
        return self.names
