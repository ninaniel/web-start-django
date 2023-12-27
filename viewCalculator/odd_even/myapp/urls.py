from django.urls import path
from myapp.views import empty_entry, odd_even

urlpatterns = [
    path('odd_or_even/', empty_entry),
    path('odd_or_even/<int:num>', odd_even)
]