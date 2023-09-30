from django.urls import path
from . import views

urlpatterns = [
    path('', views.UserProfileView.as_view()), 
    path('<int:pk>', views.UserProfileView.as_view()),  
]