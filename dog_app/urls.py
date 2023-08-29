from django.urls import path
from . import views

urlpatterns = [
    path('', views.DogView.as_view()),
    path('<int:pk>', views.DogView.as_view())
]