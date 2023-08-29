from django.urls import path
from . import views

urlpatterns = [
    path('', views.DogParkView.as_view()),
    path('<int:pk>', views.DogParkView.as_view())
]