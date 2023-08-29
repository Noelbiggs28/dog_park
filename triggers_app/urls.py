from django.urls import path
from . import views

urlpatterns = [
    path('', views.TriggerView.as_view()),
    path('<int:pk>', views.TriggerView.as_view())
]