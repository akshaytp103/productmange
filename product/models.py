from django.db import models

# Create your models here.

class productMainModel(models.Model):
    choices=(
        ("10","10"),
        ("20","20"),
        ("30","30"),
    )
    
    qualitychoices=(
        ('high','high'),
        ('low','low'),
        ('medium','medium'),
    )
    
    Title = models.CharField(max_length=50)
    Description = models.CharField(max_length=100)
    Price = models.CharField(max_length=10)
    unique_code = models.CharField(unique=True, max_length=10)
    Size = models.CharField(max_length=10,choices=choices,default=10)
    Quality= models.CharField(max_length=10,choices=qualitychoices,default='high')
    
    def __str__(self):
        return self.Title
    
    
class ProductColourModel(models.Model):
    clourchoices=(
        ("red","red"),
        ("blue","blue"),
        ("green","green"),
        ("black","black"),
    )
    
    Product=models.ForeignKey(productMainModel,on_delete=models.CASCADE)
    Colour= models.CharField(max_length=20,choices=clourchoices,default='red')
    
    def __str__(self):
        return self.Product


class ProductImageModel(models.Model):
    product= models.ForeignKey(productMainModel,on_delete=models.CASCADE)
    image= models.ImageField(upload_to ='images/')
    
    def __str__(self):
        return self.product