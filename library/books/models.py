from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=128)
    author = models.CharField(max_length=128)
    year = models.DateField(null=True)
    price = models.IntegerField(null=True)

    def __str__(self):
        return f"{self.title} {self.author}"