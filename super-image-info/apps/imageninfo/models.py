from django.db import models


class Imagen(models.Model):
    imagen = models.ImageField(upload_to="imagen")

    class Meta:
        verbose_name = "Imagen"
        verbose_name_plural = "Imagens"

    # def __unicode__(self):
    #     return self.imagen


