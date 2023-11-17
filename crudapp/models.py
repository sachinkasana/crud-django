from django.db import models

# Create your models here.
class Author(models.Model):
    name = models.CharField(max_length=255)
    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(db_column='title', max_length=100, blank=False)
    description = models.TextField(db_column='description', max_length=1000, blank=False)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    year = models.IntegerField(db_column='year',blank=False, default=2000)
    # author = models.CharField(db_column='author', max_length=100, blank=False)
   