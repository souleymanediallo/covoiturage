from django.db import models
from django.utils.text import slugify


class Stop(models.Model):
    name = models.CharField(max_length=255, unique=True)
    slug = models.SlugField(max_length=255, unique=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super(Stop, self).save(*args, **kwargs)


class BusLine(models.Model):
    number = models.CharField(max_length=10)
    departure = models.CharField(max_length=255)
    arrival = models.CharField(max_length=255)
    stops = models.ManyToManyField(Stop, through='BusStop')

    def __str__(self):
        return f"Ligne {self.number} — {self.departure} ⇔ {self.arrival}"

    def get_slug_departure(self):
        return slugify(self.departure)

    def get_slug_arrival(self):
        return slugify(self.arrival)


class BusStop(models.Model):
    line = models.ForeignKey(BusLine, on_delete=models.CASCADE)
    stop = models.ForeignKey(Stop, on_delete=models.CASCADE)
    order = models.PositiveIntegerField()

    class Meta:
        unique_together = ('line', 'stop')
        ordering = ['order']

    def __str__(self):
        return f"{self.stop.name} (Ligne {self.line.number})"
