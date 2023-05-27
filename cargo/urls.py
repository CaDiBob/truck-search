from django.urls import path
from cargo import views

urlpatterns = [
    path('cargo/<int:pk>', views.DestroyUpdateCargoView.as_view()),
    path('cargo-info/<int:pk>', views.CargoViewSet.as_view({'get': 'retrieve'})),
    path('cargo-list/', views.CargoViewSet.as_view({'get': 'list'})),
    path('add-cargo/', views.CargoViewSet.as_view({'post': 'create'})),
]
