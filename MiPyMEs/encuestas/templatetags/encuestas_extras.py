from django import template
from encuestas.models import Encuesta

register = template.Library()

@register.simple_tag
def get_encuesta_list():
    encuestas = Encuesta.objects.all()
    return encuestas