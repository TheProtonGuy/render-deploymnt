from django.db import models

class Book(models.Model):

    author = models.CharField(max_length=225)
    title = models.CharField(max_length=225)

    def __str__(self):
        return self.title