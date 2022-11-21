from django.urls import path,include


urlpatterns = [
    path('star-wars/',include('doctorapp.urls')),
]