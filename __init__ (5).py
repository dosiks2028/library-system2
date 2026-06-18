import django_filters
from .models import Book
class BookFilter(django_filters.FilterSet):
    title = django_filters.CharFilter(lookup_expr='icontains')
    author = django_filters.CharFilter(lookup_expr='icontains')
    genre = django_filters.ChoiceFilter(choices=Book.GENRE_CHOICES)
    year_min = django_filters.NumberFilter(field_name='year', lookup_expr='gte')
    year_max = django_filters.NumberFilter(field_name='year', lookup_expr='lte')
    class Meta:
        model = Book
        fields = ['title', 'author', 'genre', 'year_min', 'year_max']