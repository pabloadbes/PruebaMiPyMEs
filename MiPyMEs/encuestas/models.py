from django.db import models

# Create your models here.
class Encuesta(models.Model):
    name = models.CharField(max_length=100, verbose_name="Nombre")
    subtitle = models.CharField(max_length=200, verbose_name="Subtítulo")
    created = models.DateTimeField(verbose_name="Fecha de creación", auto_now_add=True)
    updated = models.DateTimeField(verbose_name="Fecha de última modificación", auto_now=True)

    class Meta:
        verbose_name = "encuesta"
        verbose_name_plural = "encuestas"
        ordering = ["-created"]
    
    def __str__(self) -> str:
        return self.name
    
class Seccion(models.Model):
    order = models.CharField(max_length=1, verbose_name="Orden")
    name = models.CharField(max_length=100, verbose_name="Nombre")
    subtitle = models.CharField(max_length=200, verbose_name="Subtítulo")
    encuesta = models.ForeignKey(Encuesta, verbose_name="Encuesta", on_delete=models.CASCADE)
    created = models.DateTimeField(verbose_name="Fecha de creación", auto_now_add=True)
    updated = models.DateTimeField(verbose_name="Fecha de última modificación", auto_now=True)

    class Meta:
        verbose_name = "sección"
        verbose_name_plural = "secciones"
        ordering = ["order"]
    
    def __str__(self) -> str:
        return self.name
    
class Pregunta(models.Model):
    order = models.IntegerField(verbose_name="Orden")
    name = models.CharField(max_length=200, verbose_name="Nombre")
    text = models.CharField(max_length=200, verbose_name="Texto")
    content = models.TextField(verbose_name="Contenido", null=True, blank=True)
    seccion = models.ForeignKey(Seccion, verbose_name="Sección", on_delete=models.CASCADE)
    created = models.DateTimeField(verbose_name="Fecha de creación", auto_now_add=True)
    updated = models.DateTimeField(verbose_name="Fecha de última modificación", auto_now=True)

    class Meta:
        verbose_name = "pregunta"
        verbose_name_plural = "preguntas"
        ordering = ["order"]
    
    def __str__(self) -> str:
        return self.text