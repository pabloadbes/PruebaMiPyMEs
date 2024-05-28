from django import forms
from .models import Encuesta

class EncuestaForm(forms.ModelForm):

   class Meta:
      model = Encuesta
      fields = ['name', 'subtitle']
      widgets = {
         'name': forms.TextInput(attrs={'class':'form-control'}),
         'subtitle': forms.TextInput(attrs={'class':'form-control'})
      }
      labels = {
         'name':'Nombre', 'subtitle':'Subtítulo'
      }