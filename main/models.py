from django.db import models

class items(models.Model):
    name=models.CharField(max_length=50)
    content=models.TextField()
    money=models.CharField(max_length=30)
    typ=models.CharField(max_length=10)
    
