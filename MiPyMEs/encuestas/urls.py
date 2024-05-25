from django.urls import path
from .views import EncuestasListView, EncuestaDetailView

urlpatterns = [
    path('', EncuestasListView.as_view(), name='encuestas'),
    path('<int:pk>/<slug:encuesta_slug>/', EncuestaDetailView.as_view(), name='encuesta'),
]