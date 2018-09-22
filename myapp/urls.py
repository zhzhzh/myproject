from django.urls import path
from myapp import views

urlpatterns = [
    path('add_book/', views.add_book),
    path('show_books/', views.show_books),
]