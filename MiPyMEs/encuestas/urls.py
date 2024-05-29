from django.urls import path
from .views import EncuestaListView, EncuestaDetailView, EncuestaCreate, EncuestaUpdate, EncuestaDataUpdate, EncuestaDelete

encuestas_patterns = ([
    path('', EncuestaListView.as_view(), name='encuestas'),
    path('<int:pk>/<slug:slug>/', EncuestaDetailView.as_view(), name='encuesta'),
    path('create/', EncuestaCreate.as_view(), name='create'),
    path('update/<int:pk>/', EncuestaUpdate.as_view(), name='update'),
    path('update_data/<int:pk>/', EncuestaDataUpdate.as_view(), name='update_data'),
    path('delete/<int:pk>/', EncuestaDelete.as_view(), name='delete')
], 'encuestas')