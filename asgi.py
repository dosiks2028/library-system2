from django import forms
from django.utils import timezone
from .models import BorrowRecord
from books.models import Book
class BorrowForm(forms.ModelForm):
    class Meta:
        model = BorrowRecord
        fields = ['book', 'user', 'due_date']
        widgets = {
            'book': forms.Select(attrs={'class': 'form-control'}),
            'user': forms.Select(attrs={'class': 'form-control'}),
            'due_date': forms.DateTimeInput(attrs={'class': 'form-control', 'type': 'datetime-local'}),
        }
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['book'].queryset = Book.objects.filter(available_copies__gt=0)
    def clean_due_date(self):
        due_date = self.cleaned_data.get('due_date')
        if due_date and due_date < timezone.now():
            raise forms.ValidationError('Due date cannot be in the past')
        return due_date
class ReturnForm(forms.ModelForm):
    class Meta:
        model = BorrowRecord
        fields = []