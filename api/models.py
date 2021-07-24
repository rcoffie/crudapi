from django.db import models

# Create your models here.

class Book(models.Model):
	title = models.CharField(max_length=70)
	description = models.TextField(blank=True,null=True)
	author      = models.CharField(max_length=70)


	def __str__(self):
		return self.title


