from django.db import models


class Buyer(models.Model):
    name = models.CharField(max_length=30)
    balance = models.DecimalField(max_digits=20, decimal_places=2)
    age = models.IntegerField()

    def __str__(self):
        return self.name

class Game(models.Model):
    title = models.CharField(max_length=100)
    cost = models.DecimalField(max_digits=20, decimal_places=2)
    size = models.DecimalField(max_digits=20, decimal_places=2)
    description = models.TextField()
    age_limited = models.BooleanField(default=False)
    buyer = models.ManyToManyField(Buyer, related_name="games")

    def __str__(self):
        return self.title

class Author(models.Model):
    name = models.CharField(max_length=100)
    birth_date = models.DateField()

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'authors'


class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='books')

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'books'
