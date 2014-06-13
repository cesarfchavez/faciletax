'''
Created on 12/06/2014

@author: Cesar F. Chavez
'''
from django.contrib import admin
from models import contador, contribuyente

# Register your models here.
admin.site.register(contribuyente)
admin.site.register(contador)

