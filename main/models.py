from django.db import models

class items(models.Model):
    name=models.CharField(max_length=50)
    content=models.TextField()
    img=models.CharField(max_length=50,default='')
    money=models.CharField(max_length=30,default='')
    typ=models.CharField(max_length=10)
    
