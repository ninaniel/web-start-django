from django.urls import path
from myapp.views import main, home, about, contact


urlpatterns = [
    path('website/', main ),
    path('website/home', home ),
    path('website/about', about ),
    path('website/contact', contact ),
]

