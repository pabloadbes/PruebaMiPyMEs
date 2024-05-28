from django.db import models

class Encuesta(models.Model):
    name = models.CharField(verbose_name="Nombre", max_length=200)
    subtitle = models.CharField(verbose_name="Subtítulo", max_length=200)
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de edición")

    class Meta:
        verbose_name = "encuesta"
        verbose_name_plural = "encuestas"
        ordering = ['-updated', 'name']

    def __str__(self):
        return self.name
    
class Seccion(models.Model):
    order = models.CharField(max_length=10, verbose_name="Orden")
    name = models.CharField(max_length=100, verbose_name="Nombre")
    subtitle = models.CharField(max_length=200, verbose_name="Subtítulo")
    encuesta = models.ForeignKey(Encuesta, verbose_name='Encuesta', on_delete=models.CASCADE)
    created = models.DateTimeField(verbose_name="Fecha de creación", auto_now_add=True)
    updated = models.DateTimeField(verbose_name="Fecha de última modificación", auto_now=True)

    class Meta:
        verbose_name = "sección"
        verbose_name_plural = "secciones"
        ordering = ["-created"]
    
    def __str__(self) -> str:
        return self.name
    
# class Post(models.Model):
#     title = models.CharField(max_length=200, verbose_name="Título")
#     content = models.TextField(verbose_name="Contenido")
#     published = models.DateTimeField(verbose_name="Fecha de publicación", default=now)
#     image = models.ImageField(verbose_name="Imagen", upload_to="blog", null=True, blank=True)
#     author = models.ForeignKey(User, verbose_name="Autor", on_delete=models.CASCADE)
#     categories = models.ManyToManyField(Category, verbose_name="Categorías", related_name="get_posts")
#     created = models.DateTimeField(verbose_name="Fecha de creación", auto_now_add=True)
#     updated = models.DateTimeField(verbose_name="Fecha de última modificación", auto_now=True)

#     class Meta:
#         verbose_name = "entrada"
#         verbose_name_plural = "entradas"
#         ordering = ["created"]
    
#     def __str__(self) -> str:
#         return self.title