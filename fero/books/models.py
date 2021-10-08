from django.db import models

# Create your models here.

class Author(models.Model):
    name = models.CharField(max_length=150, blank=False, default='')

class Book(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=150, blank=False, default='')
    description = models.CharField(max_length=250, blank=True, default='')
    book_genre = models.CharField(max_length=200, blank=False, default='')
    release_date = models.DateTimeField()
    author = models.ForeignKey(Author,on_delete=models.SET_NULL,blank=True,null=True)
    class Meta:
        ordering = ('name',)
