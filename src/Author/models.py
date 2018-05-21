from django.db import models

# Create your models here.
class Author(models.Model):
    first_name = models.CharField(max_length=120)
    last_name = models.CharField(max_length=120)

    def __str__(self):
        return '%s %s' % (self.first_name, self.last_name)

class Book(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    name = models.CharField(max_length=120)
    pub_date = models.DateField()
