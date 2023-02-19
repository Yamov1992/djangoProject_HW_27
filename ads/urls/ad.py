
from django.urls import path

from ads import views

urlpatterns = [
    path('', views.AdListCreateView.as_view()),
    path('<int:pk>', views.AdDetailView.as_view())
]
