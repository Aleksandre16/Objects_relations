from django.db import models


class Author(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=200)
    books = models.ManyToManyField('Book')

    def __str__(self):
        return self.name


class Book(models.Model):
    name = models.CharField(max_length=200)
    author = models.ForeignKey('Author', on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    page_count = models.IntegerField()
    categories = models.ManyToManyField('Category')
    image = models.ImageField(default=None, null=True, blank=True)
    cover_type = models.CharField(max_length=20, choices=(
        ('hardback', 'Hardback'), ('paperback', 'Paperback'), ('special', 'Special')))

    def __str__(self):
        return self.name
