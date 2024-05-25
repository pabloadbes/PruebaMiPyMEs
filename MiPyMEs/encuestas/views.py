from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from .models import Encuesta

# Create your views here.
class EncuestasListView(ListView):
    model = Encuesta
    paginate_by = 10

class EncuestaDetailView(DetailView):
    model = Encuesta