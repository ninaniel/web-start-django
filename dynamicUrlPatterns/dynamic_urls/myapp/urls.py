from django.urls import path
from myapp.views import default_greeting, greeting

urlpatterns = [
    path('greeting/', default_greeting ),
    path('greeting/<str:name>', greeting ),
]