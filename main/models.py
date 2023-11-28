from django.db import models

class items(models.Model):
    name=models.CharField(max_length=50)
    content=models.TextField()
    img=models.CharField(max_length=50,default='')
    money=models.CharField(max_length=30,default='') #money보단 price가 적절했다
    typ=models.CharField(max_length=10)

class ShoppingCart(models.Model):
    ip=models.CharField(max_length=20)
    weapone_name=models.CharField(max_length=50)
    money=models.CharField(max_length=30)
    
