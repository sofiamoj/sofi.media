from django.db import models

# Create your models here.
class Author(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Post(models.Model):
    title = models.CharField(max_length=500)
    content = models.TextField()
    author = models.ForeignKey(Author,on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title + " / " + str (self.author.id)

class Book(models.Model):
    BOOK_TYPES = (
        ('EL','electronic'),
        ('LO', 'physical book'),
    )
    title = models.CharField(max_length=500)
    published_year = models.IntegerField(default=1400)
    exists = models.BooleanField(default=True)
    book_type = models.CharField(choices=BOOK_TYPES,max_length=2)

    def __str__(self):
        return self.title + " / " + str (self.published_year) 