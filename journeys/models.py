from django.db import models


class Journey(models.Model):
    """Represents a journey to learning and acheivement
    """

    name = models.CharField(max_length=50)
    description = models.TextField()

    def __unicode__(self):
        return self.name


class Trail(models.Model):
    """Represents a portion of a journey
    """

    name = models.CharField(max_length=50)
    description = models.TextField()
    url = models.URLField(null=True, blank=True)
    journey = models.ForeignKey(Journey)

    def __unicode__(self):
        return self.name
