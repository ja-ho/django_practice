from django.db import models

# Create your models here.

class Book(models.Model):
	title = models.CharField(max_length=100)
	authors = models.ManyToManyField('Author')
	publisher = models.ForeignKey('Publisher', on_delete = models.CASCADE)
	publication_time = models.DateField()

	def __str__(self):
		return self.title

class Author(models.Model):
	name = models.CharField(max_length=50)
	salutation = models.CharField(max_length=100)
	email = models.EmailField()

	def __str__(self):
		return self.name

class Publisher(models.Model):

