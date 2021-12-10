from django.db import models
from django.utils import timezone
from datetime import datetime, date


class User(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


    
class Client(models.Model):
    client_name = models.CharField(max_length=50, blank=False, default='')
    created_at = models.DateTimeField(auto_now_add=False, auto_now=False, null=True, default='', editable=False)
    #created_at = models.BigIntegerField(max_length=50)
    created_by = models.CharField(max_length=50, default='Rohit')
    
    

    def __str__(self):
        return self.client_name



class Project(models.Model):
    project_name = models.CharField(max_length=50, blank=False, default='')
    created_at = models.DateTimeField(auto_now_add=False, auto_now=False, default=timezone.now() + timezone.timedelta(hours=3), null=True)
    created_by = models.CharField(max_length=70, default='Ganesh')
    updated_at = models.DateTimeField(auto_now_add=False, auto_now=False, default=timezone.now() + timezone.timedelta(hours=3), null=True)
    

    def __str__(self):
        return self.project_name
