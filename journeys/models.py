from django.db import models


class Journey(models.Model):
    """Represents a journey to learning and acheivement
    """

    name = models.CharField(max_length=50)
    description = models.TextField()

class Trail(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    journey = models.ForeignKey(Journey)
