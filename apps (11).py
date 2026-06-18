from django.db import models
from django.urls import reverse
from django.core.exceptions import ValidationError

class Book(models.Model):
    GENRE_CHOICES = [
        ('fiction', 'Fiction'),
        ('non-fiction', 'Non-Fiction'),
        ('science', 'Science'),
        ('history', 'History'),
        ('fantasy', 'Fantasy'),
        ('mystery', 'Mystery'),
        ('romance', 'Romance'),
        ('thriller', 'Thriller'),
        ('biography', 'Biography'),
        ('poetry', 'Poetry'),
    ]
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    isbn = models.CharField(max_length=13, unique=True)
    year = models.IntegerField()
    genre = models.CharField(max_length=20, choices=GENRE_CHOICES)
    total_copies = models.IntegerField(default=1)
    available_copies = models.IntegerField(default=1)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    def clean(self):
        if self.year < 1000 or self.year > 2025:
            raise ValidationError('Year must be between 1000 and 2025')
        if self.available_copies > self.total_copies:
            raise ValidationError('Available copies cannot exceed total copies')
    def save(self, *args, **kwargs):
        self.full_clean()
        super().save(*args, **kwargs)
    def __str__(self):
        return f"{self.title} by {self.author}"
    def get_absolute_url(self):
        return reverse('book_detail', kwargs={'pk': self.pk})
    def is_available(self):
        return self.available_copies > 0
    def borrow_book(self):
        if self.is_available():
            self.available_copies -= 1
            self.save()
            return True
        return False
    def return_book(self):
        if self.available_copies < self.total_copies:
            self.available_copies += 1
            self.save()
            return True
        return False