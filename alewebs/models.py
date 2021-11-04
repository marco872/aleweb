from django.db import models


class Topic(models.Model):

	text = models.CharField(max_length=200)

	def __str__(self):
		return self.text

# Create your models here.
class Entry(models.Model):

	topic = models.ForeignKey(Topic, on_delete=models.CASCADE)

	text = models.TextField()

	class Meta:
		verbose_name_plural = 'entries'

	def __str__(self):
		return f"{self.text [:50]}..."