from django.db import models
class todo(models.Model):
    
    assignee = models.CharField(max_length=500)
    title = models.CharField(max_length=500)
    description = models.TextField(max_length=10000)
    status = models.CharField(max_length=100,default='In_progress')
