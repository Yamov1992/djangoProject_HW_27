
from django.urls import path

from ads import views

urlpatterns = [
    path('', views.CatListCreateView.as_view()),
    path('<int:pk>', views.CatDetailView.as_view())
]
