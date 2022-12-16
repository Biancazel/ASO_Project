from django.db import models


# Create your models here.
class Message(models.Model):
    content = models.CharField(max_length=1000)
    owner = models.CharField(max_length=45)
    timestamp = models.DateTimeField()
    is_image = models.BooleanField(default=False)
