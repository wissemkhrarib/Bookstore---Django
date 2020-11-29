from django.db import models


class Author(models.Model):
    firstname = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)
    email = models.EmailField()

    def __str__(self):
        return self.firstname+' '+self.lastname


class Book(models.Model):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=1000)
    serie_number = models.IntegerField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE)






