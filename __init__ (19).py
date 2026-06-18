from django.urls import path
from . import views
urlpatterns = [
    path('', views.BorrowListView.as_view(), name='borrow_list'),
    path('my/', views.MyBorrowListView.as_view(), name='my_borrows'),
    path('create/', views.BorrowCreateView.as_view(), name='borrow_create'),
    path('<int:pk>/return/', views.BorrowReturnView.as_view(), name='borrow_return'),
]