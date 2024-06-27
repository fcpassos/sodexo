from django.urls import path


from prescription.views import home

    
urlpatterns = [
    path('', home),
]
