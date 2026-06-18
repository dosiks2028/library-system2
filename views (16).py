from django.contrib import admin
from .models import BorrowRecord
@admin.register(BorrowRecord)
class BorrowRecordAdmin(admin.ModelAdmin):
    list_display = ['book', 'user', 'borrow_date', 'due_date', 'return_date', 'status', 'fine']
    list_filter = ['status', 'borrow_date', 'due_date']
    search_fields = ['book__title', 'user__username']
    readonly_fields = ['borrow_date', 'fine']