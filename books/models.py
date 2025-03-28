from django.db import models

class Book(models.Model):
    STATUS_CHOICES = [
        ('Available', 'Available'),
        ('Checked Out', 'Checked Out'),
    ]

    book_id = models.CharField(max_length=20, unique=True)
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    genre = models.CharField(max_length=100)
    availability = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Available')

    def __str__(self):
        return self.title

