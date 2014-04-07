from django.db import models

# Create your models here.
class Movie(models.Model):
	title = models.CharField(max_length=200)
	year = models.DateField()
	tmdbId = models.IntegerField()
	posterPath = models.CharField(max_length=200)

	def __unicode__(self):
		return self.title

class Quote(models.Model):
	movie = models.ForeignKey(Movie)
	text = models.CharField(max_length=1024)

	def __unicode__(self):
		return self.text