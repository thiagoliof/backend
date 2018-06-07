from django.db import models
from django.utils.safestring import mark_safe


class Time(models.Model):
    nome = models.CharField(max_length=50)
    image = models.ImageField(upload_to='images/', blank=True) 

    def image_tag(self):
         return mark_safe('<img src="https://res.cloudinary.com/dru0khr1k/image/upload/v1/%s" />' % (self.image))

    def __str__(self):
        return self.nome

    image_tag.short_description = 'Image'

class PrimeiraFase(models.Model):
    grupo = models.CharField(max_length=1, default='')
    mandante  = models.ForeignKey('Time',  on_delete=models.CASCADE, related_name='mandante')
    visitante = models.ForeignKey('Time',  on_delete=models.CASCADE, related_name='visitante')
    data = models.DateTimeField()
    gol_mandante = models.IntegerField(verbose_name='Gol Mandante', null=True, blank=True)
    gol_visitante = models.IntegerField(verbose_name='Gol Visitante', null=True, blank=True)

    def confronto(self):
        return "%s x %s" %( self.mandante.nome, self.visitante.nome )
        

    def __str__(self):
        return "%s x %s" %( self.mandante.nome, self.visitante.nome )
