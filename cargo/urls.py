from django.urls import path
from cargo import views

urlpatterns = [
    path('cargo-list/', views.CargoInfo.as_view()),
    path('add-cargo/', views.CreateCargoView.as_view()),
]
