from django.urls import path
from . import views

urlpatterns = [
    path('', views.OwnerView.as_view()),
    path('<int:pk>', views.OwnerView.as_view())
]