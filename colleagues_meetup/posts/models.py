from django.db import models

# Create your models here.
from django.db import models


class date(models.Model):
    userid=models.IntegerField()
    event=models.TextField()
    weekday=models.TextField()
    calendarblocked=models.TextField()
    invitation_frequency=models.IntegerField()

class user(models.Model):
    name=models.TextField()
    mail=models.CharField(max_length=50)
    passw = models.TextField()
    location=models.TextField()
    division=models.TextField()
    department=models.TextField()

class datelog(models.Model):
    userid=models.IntegerField()
    eventid=models.IntegerField()
    lastdate=models.TextField()



