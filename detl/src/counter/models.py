from __future__ import unicode_literals

from django.db import models

# Create your models here.
class click(models.Model):
    title= models.CharField(max_length=120) 
    content= models.TextField()
    updated= models.DateTimeField(auto_now=True, auto_now_add=False)
    timestamp= models.DateTimeField(auto_now=False, auto_now_add=True)
    # name = models.CharField(blank = True, null = True, max_length = 120)
    # beer = models.CharField(blank = True, null = True, max_length = 120)
    # timestamp = models.DateTimeField(auto_now_add=True,auto_now = False)
    # updated = models.DateTimeField(auto_now_add=False,auto_now=True)
    # def __unicode__(self):   #python 3.3 is __str__
    #     return self.email
    def __unicode__(self):
        return self.title
    def __str__(self):
        return self.title