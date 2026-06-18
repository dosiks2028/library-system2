from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib import messages
from .models import Book
from .forms import BookForm
from .filters import BookFilter
class BookListView(LoginRequiredMixin, ListView):
    model = Book
    template_name = 'books/list.html'
    paginate_by = 10
    def get_queryset(self):
        queryset = super().get_queryset()
        self.filter = BookFilter(self.request.GET, queryset=queryset)
        return self.filter.qs
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter'] = self.filter
        return context
class BookDetailView(LoginRequiredMixin, DetailView):
    model = Book
    template_name = 'books/detail.html'
class BookCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = Book
    form_class = BookForm
    template_name = 'books/form.html'
    permission_required = 'books.add_book'
    success_url = reverse_lazy('book_list')
    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, f'Book "{form.instance.title}" created successfully!')
        return response
class BookUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = Book
    form_class = BookForm
    template_name = 'books/form.html'
    permission_required = 'books.change_book'
    success_url = reverse_lazy('book_list')
    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, f'Book "{form.instance.title}" updated successfully!')
        return response
class BookDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = Book
    template_name = 'books/delete.html'
    permission_required = 'books.delete_book'
    success_url = reverse_lazy('book_list')
    def delete(self, request, *args, **kwargs):
        book = self.get_object()
        messages.success(self.request, f'Book "{book.title}" deleted successfully!')
        return super().delete(request, *args, **kwargs)