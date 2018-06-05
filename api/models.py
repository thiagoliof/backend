from django.db import models
from django.utils.safestring import mark_safe

class Time(models.Model):
    nome = models.CharField(max_length=50)
    bandeira = models.ImageField(upload_to='./uploads')

    def image_tag(self):
        return mark_safe('<img src="/%s" />' % (self.bandeira))

    def __str__(self):
        return self.nome

    image_tag.short_description = 'Image'

class PrimeiraFase(models.Model):
    mandante  = models.ForeignKey('Time',  on_delete=models.CASCADE, related_name='mandante')
    visitante = models.ForeignKey('Time',  on_delete=models.CASCADE, related_name='visitante')
    data = models.DateTimeField()
