from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Encuesta
from .forms import EncuestaForm

# Create your views here.
class EncuestaListView(ListView):
    model = Encuesta

class EncuestaDetailView(DetailView):
    model = Encuesta

class EncuestaCreate(CreateView):
    model = Encuesta
    form_class = EncuestaForm
    success_url = reverse_lazy('encuestas:encuestas')

class EncuestaUpdate(UpdateView):
    model = Encuesta
    form_class = EncuestaForm
    template_name_suffix = "_update_form"

    def get_success_url(self) -> str:
        return reverse_lazy('encuestas:update', args=[self.object.id]) + '?ok'
    
class EncuestaDelete(DeleteView):
    model = Encuesta
    success_url = reverse_lazy('encuestas:encuestas')