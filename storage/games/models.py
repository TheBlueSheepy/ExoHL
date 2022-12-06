from django.db import models

# Create your models here.

class Studio(models.Model):
    name = models.CharField(max_length=100,unique=True)

    def __str__(self):
        return self.name

class Platform(models.Model):
    name = models.CharField(max_length=100,unique=True)

    def __str__(self):
        return self.name

class Game(models.Model):
    name = models.CharField(max_length=100, blank=False, unique=True)
    release_date = models.DateField()
    studio = models.ForeignKey(
            Studio, 
            on_delete=models.RESTRICT,
            related_name='games'
        )
    ratings = models.IntegerField()
    platforms = models.ManyToManyField(Platform)
