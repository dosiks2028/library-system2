from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from books.models import Book
from decimal import Decimal
STATUS_CHOICES = [
    ('borrowed', 'Borrowed'),
    ('returned', 'Returned'),
    ('overdue', 'Overdue'),
]
class BorrowRecord(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    borrow_date = models.DateTimeField(default=timezone.now)
    due_date = models.DateTimeField()
    return_date = models.DateTimeField(null=True, blank=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='borrowed')
    fine = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    def __str__(self):
        return f"{self.book.title} borrowed by {self.user.username} on {self.borrow_date}"
    def calculate_fine(self):
        if self.return_date:
            if self.return_date > self.due_date:
                days_overdue = (self.return_date - self.due_date).days
                return Decimal(days_overdue) * Decimal('0.50')
            return Decimal('0.00')
        if timezone.now() > self.due_date:
            days_overdue = (timezone.now() - self.due_date).days
            return Decimal(days_overdue) * Decimal('0.50')
        return Decimal('0.00')
    def return_book(self):
        if self.status != 'returned':
            self.return_date = timezone.now()
            self.fine = self.calculate_fine()
            if self.fine > 0:
                self.status = 'overdue'
            else:
                self.status = 'returned'
            self.book.return_book()
            self.save()
            return True
        return False