from django.urls import path
from truck import views

urlpatterns = [
    path('truck/<int:pk>', views.TruckUpdateView.as_view()),
]
