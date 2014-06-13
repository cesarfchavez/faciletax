from django.db import models

# Create your models here.
class contribuyente(models.Model):
    RUC = models.CharField(max_length=13, unique=True)
    razon_social = models.CharField (max_length=60)
    
    def __unicode__(self):
        return self.RUC
    
class contador(models.Model):
    nombre = models.CharField(max_length=13, unique=True)
    contribuyente = models.ForeignKey(contribuyente)
    
    def __unicode__(self):
        return self.nombre
    
    